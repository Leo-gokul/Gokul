import pandas as pd
import matplotlib.pyplot as plt
data = {
 'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
 'Sales': [100, 150, 120, 80]
}
sales_data = pd.DataFrame(data)
total_revenue = sales_data['Sales'].sum()
print("Total Revenue:", total_revenue)
average_sales = sales_data['Sales'].mean()
print("Average Daily Sales:", average_sales)
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
plt.figure(figsize=(8, 4))
plt.plot(sales_data['Date'], sales_data['Sales'], marker='o')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend Over Time')
plt.grid(True)
plt.show()
