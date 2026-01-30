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

def create_pivot_table(df):
    '''
    Creates a pivot table with month as index, category as columns, and sum of net_amount as values.
    Also adds a Grand Total column and computes month-over-month growth %.
    '''
    # Ensure order_date is in datetime format
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Extract month from order_date
    df['month'] = df['order_date'].dt.to_period('M')
    
    # Create pivot table
    # pivot_table = pd.pivot_table(df, index='month', columns='category', values='net_amount')
    pivot_table = df.pivot_table(index='month', columns='category', values='net_amount', aggfunc='sum', fill_value=0)

    
    # Add Grand Total column
    pivot_table['Grand Total'] = pivot_table.sum(axis=1)
    
    # Compute month-over-month growth %
    pivot_table['MoM Growth %'] = pivot_table['Grand Total'].pct_change() * 100
    
    return pivot_table

data = load_data("C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv")
data_with_net_amount = add_net_amount_column(data)
pivot_table = create_pivot_table(data_with_net_amount)
print(f"Pivot Table with MoM Growth %:\n{pivot_table}")

