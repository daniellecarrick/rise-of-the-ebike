import datetime
import glob
import pandas as pd

# Get all CSV files in the current directory
file_list = glob.glob("data/*.csv") 

dfs = []
for file in file_list:
    print(file)
    df = pd.read_csv(file)
    df['sourceFile'] = file
    dfs.append(df)

df = pd.concat(dfs)

# Ensure the 'started_at' column is in datetime format
df['datetimeOld'] = pd.to_datetime(df['started_at'], errors='coerce')
df['datetime'] = pd.to_datetime(df['started_at'], format='ISO8601')

# Extract the date part from the 'datetime' column
df['date'] = df['datetime'].dt.isocalendar().week

# Group by date and rideable_type, then count the ride IDs
daily_counts = df.groupby(['date', 'rideable_type']).size().unstack(fill_value=0)

# Reset the index to make it a proper DataFrame
daily_counts = daily_counts.reset_index()

# Rename columns for clarity
daily_counts.columns.name = None  # Remove the name of the index


def snapshot_data(df: pd.DataFrame, fnameStem: str):
    suffix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    fname = f'{fnameStem}-{suffix}.csv'
    df.to_csv(fname, index=False)

# Save to a new CSV file (optional)
snapshot_data(daily_counts, 'daily_ride_counts')

print(daily_counts)

