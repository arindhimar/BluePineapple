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


def group_by_city_aggregations(df):
    '''
    Groups by city and computes required aggregations
    '''
    grouped = df.groupby('city').agg(total_orders=('order_id', 'count'),
        unique_customers=('customer_id', 'nunique'),
        total_revenue=('net_amount', 'sum'),
        average_order_value=('net_amount', 'mean')
    ).reset_index()
    #reset index is to convert the groupby object back to a dataframe
    top_cities = grouped.sort_values(by='total_revenue', ascending=False).head(10)
    
    return top_cities


data = load_data("C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv")
data_with_net_amount = add_net_amount_column(data)
top_cities_aggregations = group_by_city_aggregations(data_with_net_amount)
print(f"Top 10 Cities by Revenue:\n{top_cities_aggregations}")