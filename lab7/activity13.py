import pandas as pd

employee_details = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
})

employee_salaries = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
})

sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North'] * 5,
    'Sales': [250, 300, 200, 400, 350]
})

sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South'] * 5,
    'Sales': [300, 320, 280, 360, 310]
})

print("Employee Details:\n", employee_details)
print("\nEmployee Salaries:\n", employee_salaries)

median_salary_per_dept = employee_details.merge(employee_salaries, on='Employee_ID').groupby('Department')['Salary'].median()
print("\nMedian Salary per Department:\n", median_salary_per_dept)

merged_data_outer = pd.merge(employee_details, employee_salaries, on='Employee_ID', how='outer')
print("\nMerged Data (Outer Join):\n", merged_data_outer)

stock_prices = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Price': [150, 155, 152, 158, 160]
}).set_index('Date')

market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
}).set_index('Date')

print("\nStock Prices Data:\n", stock_prices)
print("\nMarket Volume Data:\n", market_volume)

joined_stock_data = stock_prices.join(market_volume, how='inner')
print("\nJoined Stock Prices and Market Volume Data:\n", joined_stock_data)

horizontal_concat = pd.concat([sales_region_1.set_index('Date'), sales_region_2.set_index('Date')], axis=1)
print("\nHorizontally Concatenated Sales Data:\n", horizontal_concat)