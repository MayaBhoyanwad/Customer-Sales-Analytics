import sqlite3

conn = sqlite3.connect("data/analytics.db")
cursor = conn.cursor()

query = """
SELECT
    Product_ID,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(
        SUM(Profit) * 100.0 / SUM(Sales),
        2
    ) AS Profit_Margin
FROM orders
GROUP BY Product_ID
HAVING SUM(Sales) > 0
ORDER BY Profit_Margin DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\nProduct Profitability:")
print("-" * 80)

for row in results:
    print(
        "Product:", row[0],
        "| Sales:", row[1],
        "| Profit:", row[2],
        "| Margin:", row[3], "%"
    )

conn.close()