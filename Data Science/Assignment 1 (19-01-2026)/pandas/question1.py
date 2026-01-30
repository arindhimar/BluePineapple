import pandas as pd

def read_csv_file(file_path):
    '''
    Reads CSV File
    '''
    return pd.read_csv(file_path)

def convert_date_to_datetime(sample_data):
    '''
    Converts data column to date and time column
    '''
    sample_data['date'] = pd.to_datetime(sample_data['signup_date'])
    # print(sample_data.dtypes)
    return sample_data

def trim_whitespace_from_string_columns(sample):
    '''
    Trims whitespace from string columns in the dataframe
    '''
    str_cols = sample.select_dtypes(include=['object']).columns
    for col in str_cols:
        sample[col] = sample[col].str.strip()
    return sample




data = read_csv_file("C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/customers.csv")

print(data.head())
print(data.info())
print(data.describe(include="all"))
print(convert_date_to_datetime(data))
print(trim_whitespace_from_string_columns(data))