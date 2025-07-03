import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the cleaned data
all_trips_df = pd.read_csv('notebooks/2024-divvy-all-trips.csv')
all_trips_df['started_at'] = pd.to_datetime(all_trips_df['started_at'])
all_trips_df['month'] = all_trips_df['started_at'].dt.to_period('M').astype(str)

# Ensure output folder exists
os.makedirs('outputs', exist_ok=True)

# Set plot style
sns.set(style="whitegrid")

# 1. Average ride duration per month
plt.figure(figsize=(10, 5))
monthly_avg = all_trips_df.groupby('month')['ride_duration_min'].mean().reset_index()
sns.barplot(data=monthly_avg, x='month', y='ride_duration_min', color='skyblue')
plt.title('Average Ride Duration per Month')
plt.xlabel('Month')
plt.ylabel('Average Duration (min)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/avg_ride_duration_per_month.png')
plt.close()

# 2. Member vs Casual ride count
plt.figure(figsize=(6, 5))
sns.countplot(data=all_trips_df, x='member_casual', palette='Set2')
plt.title('Ride Counts: Member vs Casual')
plt.xlabel('User Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('outputs/member_vs_casual_count.png')
plt.close()

# 3. Top 10 start stations
top_starts = all_trips_df['start_station_name'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_starts.values, y=top_starts.index, palette='viridis')
plt.title('Top 10 Start Stations')
plt.xlabel('Number of Rides')
plt.ylabel('Start Station')
plt.tight_layout()
plt.savefig('outputs/top_10_start_stations.png')
plt.close()

print("\n✅ Visualizations saved to outputs/ folder.")