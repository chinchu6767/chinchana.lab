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
    'Region': ['North', 'North', 'North', 'North', 'North'],
    'Sales': [250, 300, 200, 400, 350]
})
sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South', 'South', 'South', 'South', 'South'],
    'Sales': [300, 320, 280, 360, 310]
})

print("Employee Details:")
print(employee_details)
print("\nEmployee Salaries:")
print(employee_salaries)
print("\nSales Region 1:")
print(sales_region_1)
print("\nSales Region 2:")
print(sales_region_2)

avg_salary_per_dept = employee_details.merge(employee_salaries, on='Employee_ID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary_per_dept)

merged_data = pd.merge(employee_details, employee_salaries, on='Employee_ID', how='inner')
print("\nMerged Data:")
print(merged_data)

stock_prices = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Price': [150, 155, 152, 158, 160]
})
stock_prices.set_index('Date', inplace=True)

market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
})
market_volume.set_index('Date', inplace=True)

print("Stock Prices Data:")
print(stock_prices)
print("\nMarket Volume Data:")
print(market_volume)

joined_data = stock_prices.join(market_volume, how='inner')
print("\nJoined Stock Prices and Market Volume Data:")
print(joined_data)

consolidated_sales = pd.concat([sales_region_1, sales_region_2], axis = 0)
print("\nConsolidated Sales Data:")
print(consolidated_sales)