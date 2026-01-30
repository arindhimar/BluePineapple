import pandas as pd

def load_data(file_path):
    '''
    Loads data from a CSV file
    '''
    return pd.read_csv(file_path)

def add_net_amount_column(df):
    '''
    Adds net_amount column to the dataframe
    '''
    # Compute gross_amount
    df['gross_amount'] = df['quantity'] * df['unit_price']
    
    # Compute net_amount
    df['net_amount'] = df['gross_amount'] * (1 - df['discount_pct'] / 100)
    
    return df

def filter_orders(df, categories, net_amount_threshold, days):
    '''
    Filters orders based on category, net_amount, and order_date
    '''
    # Ensure order_date is in datetime format
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Get the maximum date in the dataset
    max_date = df['order_date'].max()
    
    # Calculate the date N days before the maximum date
    date_threshold = max_date - pd.Timedelta(days=days)
    
    # Apply filters
    filtered_df = df[
        (df['category'].isin(categories)) &
        (df['net_amount'] > net_amount_threshold) &
        (df['order_date'] >= date_threshold)
    ]
    
    # Calculate count and total net_amount
    count = filtered_df.shape[0]
    total_net_amount = filtered_df['net_amount'].sum()
    
    return count, total_net_amount


data = load_data("C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv")
new_data = add_net_amount_column(data)
categories_to_filter = ['Electronics', 'Fashion']
net_amount_threshold = 100
days = 30

count, total_net_amount = filter_orders(new_data, categories_to_filter, net_amount_threshold, days)
print(f"Count of Filtered Orders: {count}")
print(f"Total Net Amount of Filtered Orders: {total_net_amount}")