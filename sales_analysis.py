# ===== E-COMMERCE SALES ANALYSIS PROJECT =====

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load dataset
df = pd.read_csv("sales_data.csv")

# Step 3: Data cleaning
df = df.drop_duplicates()               # Remove duplicate rows
df['Date'] = pd.to_datetime(df['Date']) # Convert Date column to datetime

# Step 4: Basic metrics
total_sales = df['Total_Sales'].sum()   # Total sales
total_quantity = df['Quantity'].sum()   # Total items sold

sales_by_product = df.groupby("Product")['Total_Sales'].sum()
sales_by_region = df.groupby("Region")['Total_Sales'].sum()

# Monthly sales trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# ===== Step 5: Visualizations =====

#Bar chart: Total Sales by Product
plt.figure(figsize=(8,6))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Line chart: Monthly Sales Trend
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', color='orange')
plt.title("Monthly Total Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#Pie chart: Sales Distribution by Region
plt.figure(figsize=(7,7))
sales_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title("Total Sales Distribution by Region")
plt.ylabel("")  # Remove default y label
plt.tight_layout()
plt.show()

# ===== Step 6: Insights =====
print("===== PROJECT INSIGHTS =====")
print(f"Total Sales: ₹{total_sales}")
print(f"Total Quantity Sold: {total_quantity}")

top_product = sales_by_product.idxmax()
top_product_sales = sales_by_product.max()
print(f"Top Selling Product: {top_product} (₹{top_product_sales})")

top_region = sales_by_region.idxmax()
top_region_sales = sales_by_region.max()
print(f"Region Contributing Most to Sales: {top_region} (₹{top_region_sales})")

peak_month = monthly_sales.idxmax()
peak_month_sales = monthly_sales.max()
print(f"Month with Highest Sales: {peak_month} (₹{peak_month_sales})")
