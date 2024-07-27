import pandas as pd
import os

if __name__ == "__main__":
    curr_dir = os.getcwd()
    file_name = 'com.samsung.shealth.activity.day_summary.20240713114102.csv'
    col_to_load = [4, 10, 12, 22, 24]
    file_path = curr_dir + '\\s_health\\' + file_name 

    #Read file (skip first line from the file)
    df = pd.read_csv(file_path, skiprows = 1, usecols = col_to_load)

    #Delete rows where steps = 0 
    df_series = df['step_count'] != 0
    df = df[df_series]

    print(df.columns)
    print(df.head())  # Print the first few rows of the DataFrame