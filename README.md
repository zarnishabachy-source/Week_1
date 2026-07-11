# Week 1 Assignment — RetailHub Data Analysis, Cleaning & EDA

## Overview
This project cleans and analyzes five raw RetailHub datasets (customers, products,
orders, payments, categories), merges them into a single sales table, loads it into
SQLite, and answers the business questions defined in the task brief.

## Folder Structure
```
Week1_Assignment/
├── datasets/                  Raw input files (unmodified)
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── payments.xlsx
│   └── categories.json
├── output/
│   ├── cleaned_data.csv / .xlsx / .json   Final cleaned & merged dataset
│   ├── report_sales_by_city.csv
│   ├── report_sales_by_category.csv
│   ├── report_monthly_revenue.csv
│   ├── report_product_performance.csv
│   ├── report_pivot_city_category.csv
│   └── *.png                              Charts used in the business report
├── notebook.ipynb              Full, executed analysis notebook (Parts 1-10)
├── retailhub.db                 SQLite database (tables: `sales`, `payments`)
├── sql_queries.sql              All 12 required SQL business queries
├── business_report.pdf          Executive summary with tables & visuals
├── README.md                    This file
└── requirements.txt
```

## How the data was cleaned
Every dataset went through the same pipeline (documented step-by-step in the notebook):
1. Column names lower-cased and snake_cased.
2. Whitespace stripped from all text fields.
3. Exact duplicate rows and duplicate primary keys removed.
4. Inconsistent text (gender, city, brand, payment method/status, order status)
   standardized to a single casing/spelling.
5. Columns converted to correct types (numeric, datetime).
6. **Negative, zero, and sentinel/invalid values** (e.g. age = -5, price = -100,
   stock = -5, quantity <= 0, customer_id = 9999, product_id = 8888) treated as
   invalid, converted to missing, then re-derived or imputed with the median /
   most sensible category value.
7. Missing values filled using median (numeric columns) or explicit categories
   such as `Unknown`, `Generic`, `No Payment Record` (text columns), always
   documented with the reasoning inline in the notebook.

## Key Results
- Raw datasets: 739 total rows across 5 files, ~7.95% of all cells missing, 38 duplicate rows removed.
- Final cleaned sales table: 133 valid orders, 0 missing values.
- Total revenue: PKR 7,204,923.99 | Average order value: PKR 54,172.36.
- Top city: Lahore | Top category: Category 35 | Top payment method: Cash (36 uses, from the full
  134-record payments table — JazzCash is second with 32).
- Pending payments: 37 (measured from the full payments table, not the order-joined subset).

## Note on Payment-Level Metrics
The database has two tables:

* **Sales**: Contains one row for each cleaned order.
* **Payments**: Contains all cleaned payment records.

Questions about payment methods (such as the most popular payment method or pending payments) should be answered using the **payments** table because it includes every payment.

Using the **sales** table can give incorrect results because it only keeps one payment for each order and only includes orders that passed the cleaning process.


## How to Reproduce
1. `pip install -r requirements.txt`
2. Open `notebook.ipynb` in Jupyter and run all cells (paths are relative to this folder).
3. This regenerates everything in `output/`, `retailhub.db`, and `sql_queries.sql`.
4. `business_report.pdf` summarizes the findings with charts.

