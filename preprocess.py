import pandas as pd
import numpy as np

print("Loading data...")
file_path = 'FitPulse_wearable_device_data.csv'
df = pd.read_csv(file_path)

print("Converting timestamps...")
if 'time_stamp' in df.columns:
    df['time_stamp'] = pd.to_datetime(df['time_stamp'], utc=True)
else:
    df['time_stamp'] = pd.to_datetime(df.filter(regex='(?i)time|date').iloc[:, 0], utc=True)

df.dropna(subset=['time_stamp'], inplace=True)

df.rename(columns={'Patient_ID': 'Id', 'id': 'Id'}, inplace=True)
if 'Id' not in df.columns:
    df['Id'] = 'Default_User'
df['Id'] = df['Id'].astype(str)

print("Aligning data to 1-minute intervals...")
processed_dfs = []

for user_id, user_df in df.groupby('Id'):
    user_df = user_df.sort_values('time_stamp')
    user_df.set_index('time_stamp', inplace=True)
    user_df = user_df[~user_df.index.duplicated(keep='first')]
    
    numeric_cols = user_df.select_dtypes(include=[np.number]).columns
    categorical_cols = user_df.select_dtypes(exclude=[np.number]).columns

    resampled_numeric = user_df[numeric_cols].resample('1min').mean()
    resampled_numeric = resampled_numeric.interpolate(method='time')

    if len(categorical_cols) > 0:
        resampled_cat = user_df[categorical_cols].resample('1min').ffill()
        user_resampled = pd.concat([resampled_numeric, resampled_cat], axis=1)
    else:
        user_resampled = resampled_numeric

    user_resampled.bfill(inplace=True)
    user_resampled.ffill(inplace=True)
    user_resampled['Id'] = user_id
    processed_dfs.append(user_resampled)

if processed_dfs:
    final_df = pd.concat(processed_dfs)
    final_df.reset_index(inplace=True)
    
    # Reorder columns: Id, time_stamp, then everything else
    cols = ['Id', 'time_stamp'] + [c for c in final_df.columns if c not in ['Id', 'time_stamp']]
    final_df = final_df[cols]
    
    print(f"Final Data Shape: {final_df.shape}")
    print(final_df.head())
    
    output_path = 'cleaned_fitness_data_1min.csv'
    final_df.to_csv(output_path, index=False)
    print(f"Saved 1-minute aligned data to {output_path}")
else:
    print("No data processed.")