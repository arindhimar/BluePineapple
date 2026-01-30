import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def introduce_missing_values(df):
    df.loc[df.sample(frac=0.2).index, "city"] = None
    df.loc[df.sample(frac=0.2).index, "payment_mode"] = None
    df.loc[df.sample(frac=0.2).index, "discount_pct"] = None
    return df

def fill_categorical_missing(df):
    df["city"] = df["city"].fillna("Unknown")
    df["payment_mode"] = df["payment_mode"].fillna("Unknown")
    return df

def fill_numeric_by_category_median(df, column):
    df[column] = df.groupby("category")[column].transform(
        lambda x: x.fillna(x.median())
    )
    return df

file_path = "C:/Users/Arin Dhimar/Documents/BluePineapple/Data Science/Assignment 1 (19-01-2026)/orders.csv"

data = load_data(file_path)
data = introduce_missing_values(data)
data = fill_categorical_missing(data)
data = fill_numeric_by_category_median(data, "discount_pct")

print(data.isna().sum())
