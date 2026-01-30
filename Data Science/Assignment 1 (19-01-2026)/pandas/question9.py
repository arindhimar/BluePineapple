import pandas as pd

def load_data(file_path):
    """Load data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def add_net_amount_column(df):
    """Add gross_amount and net_amount columns."""
    df['gross_amount'] = df['quantity'] * df['unit_price']
    df['net_amount'] = df['gross_amount'] * (1 - df['discount_pct'] / 100)
    return df


def flag_outliers(group, column):
    """Flag outliers in a column using IQR method."""
    Q1 = group[column].quantile(0.25)
    Q3 = group[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    group[f'{column}_outlier_before'] = group[column].apply(
        lambda x: 1 if x < lower_bound or x > upper_bound else 0
    )
    return group


def cap_outliers(group, column):
    """Cap outliers in a column using IQR bounds."""
    Q1 = group[column].quantile(0.25)
    Q3 = group[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    group[f'{column}_capped'] = group[column].apply(
        lambda x: lower_bound if x < lower_bound
        else upper_bound if x > upper_bound
        else x
    )
    return group


def flag_outliers_after(group, column):
    """Flag outliers after capping."""
    Q1 = group[column].quantile(0.25)
    Q3 = group[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    group[f'{column}_outlier_after'] = group[column].apply(
        lambda x: 1 if x < lower_bound or x > upper_bound else 0
    )
    return group

file_path = "C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv"

data = load_data(file_path)
data["order_date"] = pd.to_datetime(data["order_date"])

data = add_net_amount_column(data)

data = data.groupby("category", group_keys=False).apply(
    lambda g: flag_outliers(g, "net_amount")
)

data = data.groupby("category", group_keys=False).apply(
    lambda g: cap_outliers(g, "net_amount")
)

data = data.groupby("category", group_keys=False).apply(
    lambda g: flag_outliers_after(g, "net_amount_capped")
)


outlier_report = (
    data.groupby("category")[
        ["net_amount_outlier_before", "net_amount_capped_outlier_after"]
    ]
    .sum()
    .reset_index()
)

print(outlier_report)
