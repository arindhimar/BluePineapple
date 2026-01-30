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

def sort_values(df):
    '''
    Sorts the dataframe by customer_id and order_date
    '''
    return df.sort_values(["customer_id", "order_date"])

def add_prev_date(df):
    '''
    Adding prev date wrt order_date
    '''
    df["prev_order_date"] = df.groupby("customer_id")["order_date"].shift(1)
    return df

def days_since_prev(df):
    '''
    Computes days since previous order
    '''
    df["days_since_prev_order"] = (df["order_date"] - df["prev_order_date"]).dt.days
    return df


def rolling_3_avg_amount(df):
    '''
    Computes rolling 3-order average net_amount per customer
    '''
    df["rolling_3_avg_net_amount"] = df.groupby("customer_id")["net_amount"].transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    return df

file_path = "C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv"

data = load_data(file_path)

# Ensure datetime type (required for window functions)
data["order_date"] = pd.to_datetime(data["order_date"])

data_with_net_amount = add_net_amount_column(data)

sorted_data = sort_values(data_with_net_amount)

sorted_data = add_prev_date(sorted_data)

sorted_data = days_since_prev(sorted_data)

print("Data with days since previous order:")
print(sorted_data.head())

