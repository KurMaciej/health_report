import pandas as pd
import os

if __name__ == "__main__":
    curr_dir = os.getcwd()
    #Need to skip first line from the file
    file_name = 'com.samsung.shealth.activity.day_summary.20240713114102.csv'

    file_path = curr_dir + '\\s_health\\' + file_name 

    df = pd.read_csv(file_path, skiprows = 1)
    print(df.head())  # Print the first few rows of the DataFrame