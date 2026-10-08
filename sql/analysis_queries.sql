-- 1. Overall Business Performance

SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM orders;


-- 2. Top 10 Customers by Sales

SELECT
    Customer_ID,
    SUM(Sales) AS Total_Sales,
    COUNT(Order_ID) AS Number_of_Orders
FROM orders
GROUP BY Customer_ID
ORDER BY Total_Sales DESC
LIMIT 10;


-- 3. Top 10 Products by Sales

SELECT
    Product_ID,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Product_ID
ORDER BY Total_Sales DESC
LIMIT 10;


-- 4. Monthly Sales

SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY strftime('%Y-%m', Order_Date)
ORDER BY Month;


-- 5. Monthly Sales with MoM Growth

WITH monthly_sales AS (
    SELECT
        strftime('%Y-%m', Order_Date) AS Month,
        SUM(Sales) AS Total_Sales
    FROM orders
    GROUP BY strftime('%Y-%m', Order_Date)
)

SELECT
    Month,
    Total_Sales,
    LAG(Total_Sales) OVER (
        ORDER BY Month
    ) AS Previous_Month_Sales
FROM monthly_sales
ORDER BY Month;


-- 6. Order Status Analysis

SELECT
    Order_Status,
    COUNT(*) AS Number_of_Orders,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Order_Status;


-- 7. Product Profitability

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


-- 8. Customer Purchase Frequency

SELECT
    Customer_ID,
    COUNT(Order_ID) AS Number_of_Orders,
    SUM(Sales) AS Total_Sales,
    ROUND(AVG(Sales), 2) AS Average_Order_Value
FROM orders
GROUP BY Customer_ID
ORDER BY Number_of_Orders DESC
LIMIT 10;