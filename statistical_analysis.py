import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols

sales_df = pd.read_csv("sales_data.csv")
customer_df = pd.read_csv("customer_churn.csv")

mean_sales = sales_df['Total_Sales'].mean()
std_sales = sales_df['Total_Sales'].std()
n_sales = sales_df.shape[0]
ci_sales = stats.t.interval(0.95, df=n_sales-1, loc=mean_sales, scale=std_sales/np.sqrt(n_sales))

corr_sales_marketing = sales_df['Total_Sales'].corr(sales_df['Price'])

median_price = sales_df['Price'].median()
high_price_sales = sales_df[sales_df['Price'] > median_price]['Total_Sales']
low_price_sales = sales_df[sales_df['Price'] <= median_price]['Total_Sales']
t_stat, p_value = stats.ttest_ind(high_price_sales, low_price_sales, equal_var=False)

model = ols("Total_Sales ~ Price", data=sales_df).fit()

plt.figure(figsize=(8,5))
sns.histplot(sales_df['Total_Sales'], kde=True, color='skyblue')
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
sns.regplot(x='Price', y='Total_Sales', data=sales_df, color='orange')
plt.title("Sales vs Price (Marketing Proxy)")
plt.xlabel("Price / Marketing Spend")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(sales_df[['Price','Quantity','Total_Sales']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("\n===== STATISTICAL ANALYSIS REPORT =====")
print(f"Average Sales: ${mean_sales:,.0f} ± ${(ci_sales[1]-mean_sales):,.0f} (95% CI)")
print(f"Correlation (Sales-Marketing): {corr_sales_marketing:.2f} ", end='')
if abs(corr_sales_marketing) > 0.7:
    print("(Strong)")
elif abs(corr_sales_marketing) > 0.4:
    print("(Moderate)")
else:
    print("(Weak)")

print(f"Marketing affects sales: p = {p_value:.4f} ", end='')
if p_value < 0.05:
    print("✓ SIGNIFICANT")
else:
    print("✗ NOT SIGNIFICANT")

print("\nRegression Summary:\n", model.summary())
