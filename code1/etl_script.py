
import pandas as pd
import numpy as np
import sqlite3


orders = pd.read_csv('olist_orders_dataset.csv')
items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')

orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])

orders['days_to_delivery'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days

orders['days_to_delivery'] = orders['days_to_delivery'].fillna(0)

conn = sqlite3.connect('ecom_data.db')
orders.to_sql('fact_orders', conn, if_exists='replace', index=False)
items.to_sql('fact_order_items', conn, if_exists='replace', index=False)
products.to_sql('dim_products', conn, if_exists='replace', index=False)
conn.close()

