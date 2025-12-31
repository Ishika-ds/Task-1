import pandas as pd

df=pd.read_csv("sales_data.csv")
print("Dataset loaded successfully")

print("\n========SALES DATA REPORT==========\n")

total_revenue=df["Total_Sales"].sum()
best_selling_product=(df.groupby("Product")["Total_Sales"].sum().idxmax())
average_sales=df["Total_Sales"].mean()

print(f"Total Revenue Generated:Rs {total_revenue:,.2f}")
print(f"Average Sale Value     :Rs {average_sales:,.2f}")
print(f"Best Selling Product   :{best_selling_product}")

print("\n===================================\n")
