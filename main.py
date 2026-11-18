import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("outputs", exist_ok=True)
df = pd.read_csv("data/sales_data.csv")
print("\n--- ORIGINAL DATA ---")
print(df)
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)
df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)
df["Quantity"] = df["Quantity"].astype(int)
df["City"] = df["City"].fillna("Unknown")
df["City"] = df["City"].str.strip().str.title()
print("\n--- CLEANED DATA ---")
print(df)
print("\n--- MISSING VALUES AFTER CLEANING ---")
print(df.isnull().sum())
print("\n--- UPDATED DATA TYPES ---")
print(df.dtypes)
print("\n--- POTENTIAL DUPLICATE ORDERS ---")
potential_duplicates = df[
    df.duplicated(
        subset=[
            "Customer",
            "Product",
            "Quantity",
            "Price",
            "City"
        ],
        keep=False
    )
]
print(potential_duplicates)
df["Total_Sales"] = df["Quantity"] * df["Price"]
print("\n--- SALES CALCULATION ---")
print(
    df[
        [
            "Order_ID",
            "Product",
            "Quantity",
            "Price",
            "Total_Sales"
        ]
    ]
)
df.to_csv(
    "outputs/cleaned_sales_data.csv",
    index=False
)
print("\nCleaned dataset saved successfully!")
product_sales = df.groupby("Product")["Total_Sales"].sum()
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/sales_by_product.png")
plt.show()
city_sales = df.groupby("City")["Total_Sales"].sum()
plt.figure(figsize=(7, 7))
city_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Sales Distribution by City")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/sales_by_city.png")
plt.show()
plt.figure(figsize=(8, 5))
sns.heatmap(
    df[
        [
            "Quantity",
            "Price",
            "Total_Sales"
        ]
    ].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Sales Data Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.show()
print("\nAll visualizations saved successfully!")
print("\n--- OUTLIER DETECTION ---")
numerical_columns = [
    "Quantity",
    "Price",
    "Total_Sales"
]
for column in numerical_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]
    print(f"\nColumn: {column}")
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))
print("\n========== DATA INSIGHTS REPORT ==========")
total_sales = df["Total_Sales"].sum()
product_sales = df.groupby("Product")["Total_Sales"].sum()
city_sales = df.groupby("City")["Total_Sales"].sum()
best_product = product_sales.idxmax()
lowest_product = product_sales.idxmin()
top_city = city_sales.idxmax()
print("Total Records:", len(df))
print("Total Sales: ₹", total_sales)
print("\nBest-Selling Product:", best_product)
print("Lowest-Selling Product:", lowest_product)
print("Highest Sales City:", top_city)
print("\nProduct-wise Sales:")
print(product_sales)
print("\nCity-wise Sales:")
print(city_sales)
print("\nRemaining Missing Values:")
print(df.isnull().sum())
with open("outputs/insights_report.txt", "w") as file:
    file.write("DATA INSIGHTS REPORT\n")
    file.write("====================\n")
    file.write(f"Total Records: {len(df)}\n")
    file.write(f"Total Sales: Rs. {total_sales}\n")
    file.write(f"Best-Selling Product: {best_product}\n")
    file.write(f"Lowest-Selling Product: {lowest_product}\n")
    file.write(f"Highest Sales City: {top_city}\n")
    file.write("\nProduct-wise Sales:\n")
    file.write(product_sales.to_string())
    file.write("\n\nCity-wise Sales:\n")
    file.write(city_sales.to_string())
print("\nInsights report saved successfully!")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes[0, 0].bar(
    product_sales.index,
    product_sales.values
)
axes[0, 0].set_title("Sales by Product")
axes[0, 0].set_ylabel("Total Sales")
axes[0, 1].pie(
    city_sales.values,
    labels=city_sales.index,
    autopct="%1.1f%%"
)
axes[0, 1].set_title("Sales by City")
axes[1, 0].hist(
    df["Quantity"],
    bins=5
)
axes[1, 0].set_title("Quantity Distribution")
axes[1, 0].set_xlabel("Quantity")
axes[1, 0].set_ylabel("Frequency")
sns.heatmap(
    df[
        [
            "Quantity",
            "Price",
            "Total_Sales"
        ]
    ].corr(),
    annot=True,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Correlation Heatmap")
plt.suptitle(
    "SALES DATA ANALYSIS DASHBOARD",
    fontsize=16
)
plt.tight_layout()
plt.savefig("outputs/sales_dashboard.png")
plt.show()
print("\nSales dashboard saved successfully!")
print("\n===================================")
print("DATA CLEANING PROJECT COMPLETED!")
print("===================================")