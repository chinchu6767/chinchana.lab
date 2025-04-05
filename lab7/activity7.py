import pandas as pd

products = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 50000},
    {'name': 'Chair', 'category': 'Furniture', 'price': 3000},
    {'name': 'Book', 'category': 'Stationery', 'price': 500},
    {'name': 'Smartphone', 'category': 'Electronics', 'price': 25000},
    {'name': 'Shoes', 'category': 'Apparel', 'price': 2000}
]

df = pd.DataFrame(products)

df['discounted_price'] = df['price'] * 0.9

print(df)

