import pandas as pd
import os

curr_dir = os.getcwd()
file_name = 'com.samsung.shealth.activity.day_summary.20240713114102.csv'

df = pd.read_csv(curr_dir + '\\s_health\\' + file_name)

print(df.head())
