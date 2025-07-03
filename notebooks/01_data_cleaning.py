import pandas as pd
import os

# Step 1: Load and combine all monthly CSV files
data_folder = 'D:\google project cylcist\data'  # Make sure you run this script from the main project folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Combine all CSVs into one DataFrame
all_trips_df = pd.concat(
    [pd.read_csv(os.path.join(data_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 2: Clean the data
all_trips_df.dropna(subset=['ride_id', 'started_at', 'ended_at'], inplace=True)

# Handle datetime parsing with mixed formats safely
all_trips_df['started_at'] = pd.to_datetime(all_trips_df['started_at'], errors='coerce')
all_trips_df['ended_at'] = pd.to_datetime(all_trips_df['ended_at'], errors='coerce')

# Drop rows with invalid datetime conversion
all_trips_df.dropna(subset=['started_at', 'ended_at'], inplace=True)

# Add duration in minutes
all_trips_df['ride_duration_min'] = (all_trips_df['ended_at'] - all_trips_df['started_at']).dt.total_seconds() / 60

# Remove rows with negative or zero duration
all_trips_df = all_trips_df[all_trips_df['ride_duration_min'] > 0]

# Save for later use
os.makedirs('notebooks', exist_ok=True)
all_trips_df.to_csv('notebooks/2024-divvy-all-trips.csv', index=False)

print("\n✅ Data loaded, cleaned, and saved successfully.")
print("Shape:", all_trips_df.shape)
print("Columns:", all_trips_df.columns.tolist())
