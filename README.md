# Customer Sales Analytics

An end-to-end data analytics project that transforms raw customer, product, and order data into actionable business insights using **Python, Pandas, SQL, SQLite, and Power BI**.

## 📊 Project Overview

The Customer Sales Analytics project analyzes sales transactions to understand:

* Overall sales and profitability
* Customer purchasing behavior
* Product performance
* Monthly sales trends
* Order cancellations and returns
* Average Order Value (AOV)
* Profit margins
* Frequently purchasing customers

The project demonstrates a complete analytics workflow from **raw data → data cleaning → database → SQL analysis → visualization → Power BI dashboard**.

---

## 🎯 Business Objectives

The main objectives of this project are to:

1. Clean and validate raw sales data.
2. Analyze customer purchasing patterns.
3. Identify high-performing products.
4. Track sales and profit trends over time.
5. Analyze cancelled and returned orders.
6. Calculate important business KPIs.
7. Build an interactive Power BI dashboard for decision-making.

---

## 🛠️ Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Data processing and analysis     |
| Pandas       | Data cleaning and transformation |
| Matplotlib   | Data visualization               |
| SQL          | Business analysis and querying   |
| SQLite       | Relational database              |
| Power BI     | Interactive dashboard            |
| Git & GitHub | Version control                  |
| Excel / CSV  | Source data                      |

---

## 🔄 Project Workflow

```text
Raw Data
   ↓
Python + Pandas
   ↓
Data Cleaning & Validation
   ↓
Cleaned Dataset
   ↓
SQLite Database
   ↓
SQL Analysis
   ↓
Python Visualizations
   ↓
Power BI Dashboard
   ↓
Business Insights
```

---

## 📁 Project Structure

```text
Customer-Sales-Analytics/
│
├── data/
│   ├── raw/
│   │   ├── customers_raw.csv
│   │   ├── customer_sales_raw.xlsx
│   │   ├── orders_raw.csv
│   │   └── products_raw.csv
│   │
│   └── cleaned/
│       └── cleaned_orders.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── visualization.py
│   ├── load_to_sqlite.py
│   └── run_sql.py
│
├── database/
│   └── sales.db
│
├── visualizations/
│
├── powerbi/
│   └── Customer_Sales_Analytics.pbix
│
├── README.md
└── .gitignore
```

> File names may vary slightly depending on the final project folder structure.

---

## 🧹 Data Cleaning

Python and Pandas were used to prepare the raw sales data for analysis.

Key data-cleaning activities included:

* Handling data types
* Converting order dates to datetime format
* Checking missing values
* Removing duplicate records
* Validating sales and profit fields
* Preparing structured datasets for analysis
* Exporting cleaned data for database loading

### Data Quality Result

The cleaned orders dataset contains:

* **10,000 records**
* **14 columns**
* **0 missing values**
* **0 duplicate records**
* Properly formatted order dates

---

## 🗄️ SQL Analysis

The cleaned data was loaded into a SQLite database and analyzed using SQL.

Example analysis areas:

* Top customers by sales
* Most frequent customers
* Product-level sales performance
* Monthly sales trends
* Profit analysis
* Cancelled orders
* Returned orders
* Average Order Value

Example SQL analysis:

```sql
SELECT
    Customer_ID,
    COUNT(*) AS Total_Orders,
    SUM(Sales) AS Total_Sales,
    AVG(Sales) AS Average_Order_Value
FROM orders
GROUP BY Customer_ID
ORDER BY Total_Orders DESC
LIMIT 10;
```

---

## 📈 Key Business KPIs

The analysis produced the following major metrics:

| KPI                 |       Value |
| ------------------- | ----------: |
| Total Sales         | 271,616,065 |
| Total Profit        |  49,545,615 |
| Profit Margin       |      18.24% |
| Total Quantity      |      18,864 |
| Average Order Value |   27,161.61 |
| Total Orders        |      10,000 |

---

## 👥 Customer Insights

The analysis identified customers with high purchasing frequency and sales contribution.

### Most Frequent Customer

**Customer:** `CUST1717`

* Orders: **14**
* Sales: **384,775**
* Average Order Value: **27,483.93**

Customer-level analysis can help businesses identify valuable customers and develop targeted retention strategies.

---

## 📦 Product Insights

Product performance was analyzed using sales, profit, and quantity metrics.

### Top Product by Sales

**Product:** `P001`

* Sales: **77,645,750**
* Profit: **11,345,750**
* Quantity Sold: **1,275**

Product-level analysis helps identify high-performing products and supports inventory and sales planning.

---

## 📅 Monthly Sales Analysis

Monthly sales trends were analyzed to identify changes in business performance.

One notable period was:

**August 2026**

* Sales: **15,836,845**
* Month-over-Month Growth: **28.53%**

This type of trend analysis can help identify periods of strong or weak business performance.

---

## 🔄 Cancellation & Return Analysis

The project also analyzes cancelled and returned orders.

### Cancelled Orders

* Orders: **378**
* Sales: **8,918,340**
* Profit: **1,628,390**

### Returned Orders

* Orders: **301**
* Sales: **7,751,245**
* Profit: **1,443,095**

Monitoring cancellations and returns can help businesses identify operational issues and potential revenue leakage.

---

## 📊 Power BI Dashboard

The cleaned and analyzed data was connected to Power BI to create an interactive sales analytics dashboard.

The dashboard provides insights into:

* Total Sales
* Total Profit
* Profit Margin
* Quantity
* Average Order Value
* Monthly sales trends
* Product performance
* Customer performance
* Order status
* Returns and cancellations

### Dashboard Preview

Add your Power BI dashboard screenshot here:

```text
![Customer Sales Analytics Dashboard](images/dashboard.png)
```

---

## 💡 Key Business Insights

Based on the analysis:

1. The business generated approximately **271.6M in total sales**.
2. Total profit was approximately **49.5M**, resulting in an **18.24% profit margin**.
3. Product `P001` was the strongest contributor to sales.
4. `CUST1717` had the highest order frequency in the analyzed dataset.
5. August 2026 showed significant month-over-month sales growth.
6. Cancelled and returned orders represented significant sales values and should be monitored.
7. Customer and product-level analysis can support targeted business decisions.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/MayaBhoyanwad/Customer-Sales-Analytics.git
```

### 2. Navigate to the project

```bash
cd Customer-Sales-Analytics
```

### 3. Install required Python libraries

```bash
pip install pandas matplotlib openpyxl
```

### 4. Run data cleaning

```bash
python python/data_cleaning.py
```

### 5. Generate visualizations

```bash
python python/visualization.py
```

### 6. Load data into SQLite

```bash
python python/load_to_sqlite.py
```

### 7. Run SQL analysis

```bash
python python/run_sql.py
```

### 8. Open the Power BI file

Open the `.pbix` file in Power BI Desktop and refresh the data if required.

---

## 📌 Skills Demonstrated

This project demonstrates practical experience with:

* Python
* Pandas
* Data Cleaning
* Exploratory Data Analysis
* SQL
* SQLite
* Data Visualization
* Power BI
* KPI Development
* Business Analysis
* Git
* GitHub
* Data-driven Decision Making

---

## 👩‍💻 Author

**Maya Bhoyanwad**

Software Engineer | Python | Django | FastAPI | SQL | Power BI | Data Analytics

📍 Pune, Maharashtra, India

---

## ⭐ Project Purpose

This project was developed as a portfolio project to demonstrate an end-to-end approach to solving a real-world business analytics problem using Python, SQL, and Power BI.
