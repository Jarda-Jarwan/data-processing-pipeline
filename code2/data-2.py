import pandas as pd
import numpy as np

df = pd.read_csv('Messy_Employee_dataset.csv')


df[['Department', 'Region']] = df['Department_Region'].str.split('-', expand=True)
df.drop(columns=['Department_Region'], inplace=True)

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Salary'] = df['Salary'].round(2).astype(str).str.replace('.', ',', regex=False)

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)

df['Phone'] = df['Phone'].astype(str).str.replace('-', '').str.replace('.0', '', regex=False)

df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

df.drop_duplicates(inplace=True)

df.to_csv('Cleaned_Employee_dataset.csv', index=False)

