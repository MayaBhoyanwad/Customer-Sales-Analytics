import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/orders_cleaned.csv")

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Dataset Shape:", df.shape)

# -----------------------------
# 1. Total Sales
# -----------------------------
total_sales = df["Sales"].sum()

print("\nTotal Sales:", total_sales)

# -----------------------------
# 2. Total Profit
# -----------------------------
total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

# -----------------------------
# 3. Total Quantity Sold
# -----------------------------
total_quantity = df["Quantity"].sum()

print("Total Quantity Sold:", total_quantity)

# -----------------------------
# 4. Profit Margin
# -----------------------------
profit_margin = (total_profit / total_sales) * 100

print("Profit Margin:", round(profit_margin, 2), "%")

# -----------------------------
# 5. Sales by Product
# -----------------------------
product_sales = (
    df.groupby("Product_ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Products by Sales:")
print(product_sales.head(10))

# -----------------------------
# 6. Profit by Product
# -----------------------------
product_profit = (
    df.groupby("Product_ID")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Products by Profit:")
print(product_profit.head(10))

# -----------------------------
# 7. Sales by Customer
# -----------------------------
customer_sales = (
    df.groupby("Customer_ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Customers:")
print(customer_sales.head(10))

# -----------------------------
# 8. Sales by Payment Mode
# -----------------------------
payment_sales = (
    df.groupby("Payment_Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Payment Mode:")
print(payment_sales)

# -----------------------------
# 9. Sales by Order Status
# -----------------------------
status_sales = (
    df.groupby("Order_Status")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Order Status:")
print(status_sales)

# -----------------------------
# 10. Monthly Sales
# -----------------------------
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)