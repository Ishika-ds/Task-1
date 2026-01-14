import pandas as pd
import matplotlib.pyplot as plt

#load datasets
sales_df=pd.read_csv("sales_data.csv")
customer_df=pd.read_csv("customer_churn.csv")

#view starting lines
print(sales_df.head(),"\n")
print(customer_df.head(),"\n")

#check data structure and datatypes
sales_df.info()
print("\n")
customer_df.info()
print("\n")
#check missing value
print(sales_df.isnull().sum(),"\n")
print(customer_df.isnull().sum(),"\n")

#Convert Date column to datetime
#Converts Date column from string to datetime so we can extract year/month/day
sales_df["Date"]=pd.to_datetime(sales_df["Date"])

#Extract Year and Month

sales_df["Year"]=sales_df["Date"].dt.year  #Creates a new column Year from the Date column.
sales_df["Month"]=sales_df["Date"].dt.month #Creates a new column Month with month names (January, February, etc.)

#Clean text columns
sales_df["Product"]=sales_df["Product"].str.lower()    #Converts all product names to lowercase for consistency
sales_df["Region"]=sales_df["Region"].str.strip()      #Removes extra spaces from region names

#Create calculated sales column
sales_df["Calculated_Sales"]=sales_df["Quantity"]* sales_df["Price"]  #Manually calculates sales amount to validate Total_Sales

#Fix column name mismatch before merge
customer_df.rename(columns={"CustomerID":"Customer_ID"},inplace=True) #rename CustomerID to Customer_ID so both datasets have the same key column.

#Merge sales and customer data
merged_df=pd.merge(
    sales_df,
    customer_df,              #Combines sales data with customer churn data:
    on="Customer_ID",                  #on="Customer_ID" → common key
    how="left"                        #inner → keeps only matching customers
)
print(merged_df.head(),"\n")
merged_df["Churn"] = merged_df["Churn"].fillna("Unknown")
#Identify top customers
top_customers=merged_df.groupby("Customer_ID")["Total_Sales"].sum()   #Groups data by customer and calculates total sales per customer
top_customers=top_customers.sort_values(ascending=False)              #Sorts customers from highest to lowest spending
print(top_customers.head(10))                                          #Displays top 10 customers

#Calculate key business metrics
total_revenue=merged_df["Total_Sales"].sum()       #Calculates total revenue
total_customer=merged_df["Customer_ID"].nunique()  #Counts unique customers
avg_order_value=merged_df["Total_Sales"].mean()    #Calculates average order value

#Monthly sales analysis
monthly_sales=merged_df.groupby("Month")["Total_Sales"].sum()       #Calculates total sales for each month

#Best-selling products
best_products=merged_df.groupby("Product")["Quantity"].sum()         #Finds total quantity sold per product
best_products=best_products.sort_values(ascending=False)             #Sorts products from most sold to least

#Pivot table: Product × Region
pivot_product_region=pd.pivot_table(
    merged_df,
    index="Product",
    columns="Region",
    values="Total_Sales",
    aggfunc="sum"
)

#Pivot table: Month × Region
pivot_month_region=pd.pivot_table(
    merged_df,
    index="Month",
    columns="Region",
    values="Total_Sales"
)

#Visualization: Top customers
if not top_customers.empty:
    top_customers.head(5).plot(kind="bar", title="Top 5 Customers")
plt.show()                                #Creates bar chart for top 5 customers by sales

#Visualization: Monthly sales trend
monthly_sales.plot(kind="line",title="Monthly sales Trend")
plt.show()

#Visualization: Region-wise sales
merged_df.groupby("Region")["Total_Sales"].sum().plot(
    kind="bar",title="Sales by Region"
)
plt.show()

#Visualization: Churn distribution
print(merged_df["Churn"].value_counts())
merged_df["Churn"].value_counts().plot(                                     #Pie chart showing churned vs retained customers.
    kind="pie",
    autopct="%1.1f%%",
    title="Customer Churn Distribution"
)

plt.ylabel("")                          #Removes extra label and displays chart
plt.show()
