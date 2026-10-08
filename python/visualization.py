import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/processed/orders_cleaned.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -----------------------------
# 1. Monthly Sales Trend
# -----------------------------

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/processed/monthly_sales.png")
plt.show()


# -----------------------------
# 2. Top 10 Products
# -----------------------------

product_sales = (
    df.groupby("Product_ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("data/processed/top_products.png")
plt.show()


# -----------------------------
# 3. Payment Mode Analysis
# -----------------------------

payment_sales = (
    df.groupby("Payment_Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
payment_sales.plot(kind="bar")

plt.title("Sales by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("data/processed/payment_mode_sales.png")
plt.show()


print("Visualizations created successfully!")