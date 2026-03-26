import pandas as pd
import numpy as np


customers = pd.read_csv('customers.csv')
products = pd.read_csv('products.csv')
campaigns = pd.read_csv('campaigns.csv')
transactions = pd.read_csv('transactions.csv')
events = pd.read_csv('events.csv')

customers['signup_date'] = pd.to_datetime(customers['signup_date'])
products['launch_date'] = pd.to_datetime(products['launch_date'])
campaigns['start_date'] = pd.to_datetime(campaigns['start_date'])
campaigns['end_date'] = pd.to_datetime(campaigns['end_date'])
transactions['timestamp'] = pd.to_datetime(transactions['timestamp'])
events['timestamp'] = pd.to_datetime(events['timestamp'])

events['product_id'] = events['product_id'].fillna(0).astype(int)

customers['customer_id'] = customers['customer_id'].astype(int)
transactions['customer_id'] = transactions['customer_id'].astype(int)
events['customer_id'] = events['customer_id'].astype(int)

customers.to_csv('cleaned_customers.csv', index=False)
products.to_csv('cleaned_products.csv', index=False)
campaigns.to_csv('cleaned_campaigns.csv', index=False)
transactions.to_csv('cleaned_transactions.csv', index=False)
events.to_csv('cleaned_events.csv', index=False)