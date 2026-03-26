import numpy as np
import pandas as pd

df = pd.read_csv("dirty_cafe_sales.csv")

df = df.drop_duplicates()

numeric_cols = ["Quantity", "Price Per Unit", "Total Spent"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

dalsi_cols = ["Item", "Payment Method", "Location"]
for col in dalsi_cols:
    if col in df.columns:
     df[col] = df[col].fillna("Unknown")


df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]

df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")

df = df.dropna(subset=["Price Per Unit", "Transaction Date"])

df.to_csv('Cleaned_Cafe_Sales_dataset.csv', index=False)
