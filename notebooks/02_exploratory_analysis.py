# notebooks/02_exploratory_analysis.py

import pandas as pd
import os

# Load the cleaned data
all_trips_df = pd.read_csv('notebooks/2024-divvy-all-trips.csv')

# Fix datetime issues
all_trips_df['started_at'] = pd.to_datetime(all_trips_df['started_at'], errors='coerce')
all_trips_df['ended_at'] = pd.to_datetime(all_trips_df['ended_at'], errors='coerce')
all_trips_df.dropna(subset=['started_at', 'ended_at'], inplace=True)

# Add new columns
all_trips_df['month'] = all_trips_df['started_at'].dt.to_period('M')

# Summary 1: Average ride duration per month
avg_duration = all_trips_df.groupby('month')['ride_duration_min'].mean().reset_index()
print("\n📊 Average Ride Duration per Month:\n", avg_duration)

# Summary 2: Top 10 start stations
top_starts = all_trips_df['start_station_name'].value_counts().head(10)
print("\n📍 Top 10 Start Stations:\n", top_starts)

# Summary 3: Member vs Casual ride count
user_type_counts = all_trips_df['member_casual'].value_counts()
print("\n👥 Member vs Casual Users:\n", user_type_counts)

# Summary 4: Average ride duration by user type
avg_by_user_type = all_trips_df.groupby('member_casual')['ride_duration_min'].mean()
print("\n⏱️ Average Ride Duration by User Type:\n", avg_by_user_type)

# Save summaries
os.makedirs('summary_tables', exist_ok=True)
avg_duration.to_csv('summary_tables/avg_duration_by_month.csv', index=False)
top_starts.to_csv('summary_tables/top_10_start_stations.csv')
user_type_counts.to_csv('summary_tables/member_vs_casual.csv')
avg_by_user_type.to_csv('summary_tables/avg_duration_by_user_type.csv')
