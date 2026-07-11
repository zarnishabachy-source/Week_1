# NumPy E-Commerce Data Analysis

## Project Overview

This project demonstrates how to analyze an e-commerce dataset using **NumPy**. The analysis includes loading the dataset, exploring its structure, handling missing values, filtering records, removing duplicate rows, performing vectorized calculations, applying broadcasting, and generating statistical insights. All operations are implemented using NumPy without using loops wherever possible.

---

# Dataset Information

The dataset contains information about products sold in an e-commerce store.

### Dataset Columns

| Column | Description |
|---------|-------------|
| Product ID | Unique identifier for each product |
| Product Name | Name of the product |
| Category | Product category |
| Price | Product price |
| Quantity | Number of units sold |
| Rating | Customer rating |
| Revenue | Revenue generated |
| Discount | Discount percentage |

---

# Library Used

```python
import numpy as np
```

---

# Task 1: Load and Explore the Dataset

## Objective

Load the CSV dataset using NumPy and examine its basic structure.

### Functions Used

- `np.genfromtxt()`

### Results

- **Number of Rows:** 62
- **Number of Columns:** 8
- **Dataset Shape:** (62, 8)

### First Five Records

| Product ID | Product Name | Category | Price | Quantity | Rating | Revenue | Discount |
|------------|--------------|----------|-------|----------|--------|---------|----------|
| 101 | Smartphone A | Electronics | 500 | 10 | 4.5 | 5000 | 10 |
| 102 | Laptop B | Electronics | 1200 | 5 | 4.7 | 6000 | 15 |
| 103 | Headphones C | Electronics | 150 | Missing | 4.2 | 750 | 5 |
| 104 | Mouse D | Electronics | 20 | 50 | 4.0 | 1000 | 20 |
| 105 | Keyboard E | Electronics | 45 | 30 | 3.8 | 1350 | 10 |

---

# Task 2: Extract Columns

## Objective

Separate categorical and numerical data for further analysis.

### String Columns

- Product ID
- Product Name
- Category

### Numerical Columns

- Price
- Quantity
- Rating
- Revenue
- Discount

The numerical columns are loaded separately and converted into floating-point arrays.

---

# Task 3: Handle Missing Values

## Objective

Identify and replace missing values.

### Missing Values Found

| Column | Missing Values | Replacement Method |
|---------|---------------:|-------------------|
| Price | 1 | Mean |
| Quantity | 1 | 0 |
| Rating | 5 | Median |
| Discount | Missing values replaced with 0 |

### Result

All missing values were successfully replaced.

---

# Task 4: Indexing and Filtering

## Objective

Filter the dataset using Boolean masking.

### Electronics Products

A total of **27 products** belong to the **Electronics** category.

### Products with Rating Greater Than 4

A total of **49 products** have ratings greater than **4.0**.

### Products with Revenue Greater Than 10000

| Product |
|----------|
| Outlier Phone |

### Products with Discount Greater Than 20%

- Speaker J
- Watch J
- Cheap Item
### Results

| Filter Applied | Result |
|----------------|--------|
| Electronics Category | **27 Products Found** |
| Products with Rating > 4 | **49 Products Found** |
| Products with Revenue > 10000 | **1 Product Found (Outlier Phone)** |
| Products with Discount > 20% | **3 Products Found (Speaker J, Watch J, Cheap Item)** |

### Interpretation

- The dataset contains **27 products** in the **Electronics** category.
- A total of **49 products** have customer ratings greater than **4.0**, indicating high customer satisfaction.
- Only **one product**, **Outlier Phone**, generated revenue greater than **10,000**, making it a significant outlier in terms of sales.
- **Three products** offer discounts greater than **20%**:
  - Speaker J
  - Watch J
  - Cheap Item

**Console Output**

```text
Task 4: Indexing and Filtering

Electronics Products:
27 Products Found

Products with Rating > 4:
49 Products Found

Products with Revenue > 10000:
Outlier Phone

Products with Discount > 20%:
Speaker J
Watch J
Cheap Item
```

---

# Task 5: Detect and Remove Duplicate Rows

## Objective

Identify duplicate rows and remove them.

### Method Used

- Convert each row into a string.
- Use `np.unique()` to identify duplicate rows.
- Keep only unique records.

### Result

| Description | Value |
|-------------|------:|
| Total Duplicate Rows Found | 2 |
| Remaining Unique Records | 60 |

Duplicate rows were successfully removed before performing further analysis.

---

# Task 6: Vectorized Operations

## Objective

Perform calculations efficiently without using loops.

### Calculations

#### Revenue

```
Revenue = Price × Quantity
```

#### Discounted Price

```
Discounted Price = Price × (1 − Discount / 100)
```

#### Profit

```
Profit = Revenue × 25%
```

#### Tax

```
Tax = Revenue × 15%
```

### Result
| Description | Output |
|-------------|--------|
| Revenue Array Size | 60 Products |
| Projection Scenarios | 4 |
| Projected Revenue Matrix Shape | **(60, 4)** |

### Interpretation

The revenue array was successfully broadcast with four multipliers (1.0, 1.1, 1.2, and 0.9), producing a projected revenue matrix of shape **(60, 4)**. Each row represents one product, while each column represents a different revenue projection scenario.

**Console Output**

```text
Task 6: Broadcasting
Projected Revenue Shape (N, 4): (60, 4)
```
Vectorized calculations were completed successfully.

---

# Task 7: Broadcasting

## Objective

Project revenue using multiple growth scenarios.

### Multipliers Used

- 100%
- 110%
- 120%
- 90%

### Result

| Description | Value |
|-------------|-------|
| Projected Revenue Shape | (60, 4) |

This indicates that projected revenue was calculated for **60 unique products** under **4 different scenarios** simultaneously using NumPy broadcasting.

---

# Task 8: Mathematical Analysis

## Objective

Generate descriptive statistics after cleaning the dataset.

### Final Statistics (Negative Revenue Replaced with Zero)

| Metric | Value |
|--------|------:|
| Total Revenue | 208,435.15 |
| Average Revenue | 3,473.92 |
| Maximum Revenue | 40,000.00 |
| Minimum Revenue | 0.00 |
| Revenue Standard Deviation | 5,505.67 |
| Best-selling Product | Cheap Item |
| Highest-rated Product | Extreme Item |

---

# Comparison: Revenue Statistics Before and After Handling Negative Revenue

To evaluate the effect of data cleaning, revenue statistics were calculated under two different scenarios.

1. Revenue calculated directly using **Price × Quantity** (allowing negative values).
2. Revenue calculated after replacing all negative revenue values with **0**.

| Metric | Before Replacing Negative Revenue | After Replacing Negative Revenue with 0 |
|--------|----------------------------------:|----------------------------------------:|
| Total Revenue | **205,835.15** | **208,435.15** |
| Average Revenue | **3,430.59** | **3,473.92** |
| Maximum Revenue | **40,000.00** | **40,000.00** |
| Minimum Revenue | **-1,000.00** | **0.00** |
| Revenue Standard Deviation | **5,536.33** | **5,505.67** |
| Best-selling Product | **Cheap Item (Qty = 1000)** | **Cheap Item (Qty = 1000)** |
| Highest-rated Product | **Extreme Item (Rating = 5.0)** | **Extreme Item (Rating = 5.0)** |

### Observations

- Replacing negative revenue values with **0** increased the total revenue from **205,835.15** to **208,435.15**.
- The average revenue increased because negative values no longer reduced the mean.
- The minimum revenue became **0**, eliminating invalid negative revenue values.
- The revenue standard deviation decreased slightly, indicating a more consistent distribution.
- The best-selling and highest-rated products remained unchanged.

---

# NumPy Functions Used

- `np.genfromtxt()`
- `np.isnan()`
- `np.nanmean()`
- `np.nanmedian()`
- `np.where()`
- `np.unique()`
- `np.sum()`
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.std()`
- `np.argmax()`

---

# NumPy Concepts Covered

- Loading CSV files
- Data Exploration
- Array Indexing
- Boolean Masking
- Missing Value Handling
- Duplicate Detection
- Vectorized Operations
- Broadcasting
- Statistical Analysis
- Data Cleaning

---

# Conclusion

This project successfully demonstrates how **NumPy** can be used for efficient data preprocessing and analysis on an e-commerce dataset. The dataset was explored, cleaned by handling missing values and duplicate records, and analyzed using vectorized operations without loops. Broadcasting was used to generate projected revenue under multiple scenarios, while descriptive statistics provided insights into the overall sales performance. Additionally, the impact of replacing negative revenue values with zero was evaluated through a comparative analysis, resulting in cleaner and more reliable statistical outcomes.