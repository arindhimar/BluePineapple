# Joins / Merges (Customers + Orders)
# Create a customers DataFrame: customer_id , signup_date , segment .
# Merge with orders.
# Compute revenue by segment and retention proxy:
# “active in last 60 days” per segment

import pandas as pd



def load_data(file_path1, file_path2):
    '''
    Loads data from two CSV files and merges them on 'order_id'
    '''
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)
    merged_df = pd.merge(df1, df2, on='customer_id', how='left')
    return merged_df


def compute_revenue(df):
    '''
    Computes revenue for each order
    '''
    df['gross_amount'] = df['quantity'] * df['unit_price']
    df['net_amount'] = df['gross_amount'] * (1 - df['discount_pct'] / 100)
    return df

def get_revenue_by_segment(df):
    '''
    Computes total revenue by customer segment
    '''
    df = compute_revenue(df)
    revenue_by_segment = df.groupby('segment')['net_amount'].sum().reset_index()
    return revenue_by_segment


def compute_retention(df, days=60):
    '''
    Computes retention proxy: customers active in the last 'days' days
    '''
    df['order_date'] = pd.to_datetime(df['order_date'])
    recent_date = df['order_date'].max() - pd.Timedelta(days=days)
    active_customers = df[df['order_date'] >= recent_date]['customer_id'].nunique()
    total_customers = df['customer_id'].nunique()
    retention_rate = (active_customers / total_customers) * 100
    return retention_rate

file_path1 = "C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv"
file_path2 = "C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/customers.csv"

data = load_data(file_path1, file_path2)

print(f"Merged Data:\n{data.head()}")
revenue_by_segment = get_revenue_by_segment(data)
print(f"Revenue by Segment:\n{revenue_by_segment}")
retention_rate = compute_retention(data)
print(f"Retention Rate (active in last 60 days): {retention_rate:.2f}%")

