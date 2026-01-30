import pandas as pd

def load_data(file_path):
    '''
    Loads data from a CSV file
    '''
    return pd.read_csv(file_path)

def add_derived_columns(df, threshold):
    '''
    Adds derived columns to the dataframe
    '''
    # Compute gross_amount
    df['gross_amount'] = df['quantity'] * df['unit_price']
    
    # Compute net_amount
    df['net_amount'] = df['gross_amount'] * (1 - df['discount_pct'] / 100)
    
    # Add is_high_value flag
    df['is_high_value'] = df['net_amount'] > threshold
    
    return df

data = load_data("C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv")
print("Original Data:")
print(data.head())

threshold_value = 100  
data_with_derived_columns = add_derived_columns(data, threshold_value)
print("\nData with Derived Columns:")
print(data_with_derived_columns.head())