import os
import pandas as pd

# Specify the root directory where your HPC job log dataset is located
root_directory = '../data'

# Iterate through each month folder
for month_folder in os.listdir(root_directory):
    month_path = os.path.join(root_directory, month_folder)

    if os.path.isdir(month_path):
        # Construct the file path based on the pattern
        file_path = os.path.join(month_path, 'plugin=job_table/metric=job_info_marconi100/a_0_filter123_singlenode.csv')

        if os.path.exists(file_path):
            # Specify the dtype for columns 
            column_dtypes = {'resv_name': object}
            
            df = pd.read_csv(file_path, dtype=column_dtypes)
                        
            # Filter rows where start_time + runtime is not equal to end_time
            invalid_rows = df[~((pd.to_datetime(df['start_time']) + pd.to_timedelta(df['run_time'], unit='s')) == pd.to_datetime(df['end_time']))]

            # Print the invalid rows
            if not invalid_rows.empty:
                print(f'Invalid rows in {month_folder}:')
                print(invalid_rows)
                print('\n---\n')