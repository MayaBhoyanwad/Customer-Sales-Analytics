import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/orders_raw.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Remove duplicate records
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# 2. Convert Order_Date to date
# -----------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -----------------------------
# 3. Handle missing Discount
# -----------------------------
df["Discount"] = df["Discount"].fillna(0)

# -----------------------------
# 4. Handle missing Payment_Mode
# -----------------------------
df["Payment_Mode"] = df["Payment_Mode"].fillna("Unknown")

# -----------------------------
# 5. Check missing values
# -----------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# 6. Check duplicates
# -----------------------------
print("\nDuplicate Rows:", df.duplicated().sum())

# -----------------------------
# 7. Check data types
# -----------------------------
print("\nData Types:")
print(df.dtypes)

# -----------------------------
# 8. Create processed folder
# -----------------------------
import os

os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# 9. Save cleaned dataset
# -----------------------------
df.to_csv("data/processed/orders_cleaned.csv", index=False)

print("\nCleaned data saved successfully!")
print("Final Shape:", df.shape)