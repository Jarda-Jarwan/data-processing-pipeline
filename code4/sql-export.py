

import pandas as pd
import sqlite3

conn = sqlite3.connect('projekt_data.db')


customers = pd.read_csv('cleaned_customers.csv')
products = pd.read_csv('cleaned_products.csv')
campaigns = pd.read_csv('cleaned_campaigns.csv')
transactions = pd.read_csv('cleaned_transactions.csv')
events = pd.read_csv('cleaned_events.csv')


customers.to_sql('customers', conn, if_exists='replace', index=False)
products.to_sql('products', conn, if_exists='replace', index=False)
campaigns.to_sql('campaigns', conn, if_exists='replace', index=False)
transactions.to_sql('transactions', conn, if_exists='replace', index=False)
events.to_sql('events', conn, if_exists='replace', index=False)

