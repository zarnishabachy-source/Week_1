import numpy as np

# TASK 1: Load and Explore the Dataset

#load dataset
file_name = r"C:\Users\User\Downloads\numpy_ecommerce.csv"

# Load the dataset using genfromtxt with appropriate parameters
raw_data = np.genfromtxt(file_name, delimiter=",", dtype=str, skip_header=1)
# Print the number of rows, columns, and dataset shape
print("Task 1: Load and Explore")
print("Number of rows:", raw_data.shape[0])
print("Number of columns:", raw_data.shape[1])
print("Dataset shape:", raw_data.shape)
print("\nFirst five rows of data:\n", raw_data[:5])


# TASK 2: Indexing and Filtering

# Extracting numerical columns
product_ids = raw_data[:, 0]
product_names = raw_data[:, 1]
categories = raw_data[:, 2]

# Extracting numerical columns and converting to float, handling missing values
price = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=3, missing_values='', filling_values=np.nan)
quantity = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=4, missing_values='', filling_values=np.nan)
rating = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=5, missing_values='', filling_values=np.nan)
revenue_col = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=6, missing_values='', filling_values=np.nan)
discount = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=7, missing_values='', filling_values=np.nan)

# TASK 3: Missing Values 

print("\nTask 3: Missing Values Count")
print("Missing values in Price:", np.isnan(price).sum())
print("Missing values in Quantity:", np.isnan(quantity).sum())
print("Missing values in Rating:", np.isnan(rating).sum())

# Replacing missing values
mean_price = np.nanmean(price)
median_rating = np.nanmedian(rating)

price[np.isnan(price)] = mean_price
rating[np.isnan(rating)] = median_rating
quantity[np.isnan(quantity)] = 0
discount[np.isnan(discount)] = 0  # 0% discount for missing discounts

print("Missing values replaced successfully.")

# TASK 3: Indexing and Filtering

print("\nTask 3: Indexing and Filtering")

# 1. Electronics category
electronics_mask = (categories == "Electronics")
print("Electronics Products:", product_names[electronics_mask])

# 2. Rating > 4
print("Products with Rating > 4:", product_names[rating > 4])

# 3. Revenue > 10000 

safe_rev = np.where(np.isnan(revenue_col), 0, revenue_col)
print("Products with Revenue > 10000:", product_names[safe_rev > 10000])

# 4. Discount > 20%
print("Products with Discount > 20%:", product_names[discount > 20])

# TASK 4: Duplicate Rows

print("\nTask 4: Duplicate Rows")
# Build a structured view of full rows (as strings) to detect duplicates
row_strings = np.array([",".join(row) for row in raw_data])
unique_rows, unique_indices, counts = np.unique(row_strings, return_index=True, return_counts=True)

total_duplicates = np.sum(counts[counts > 1] - 1)
print("Total duplicate rows counted:", total_duplicates)

# Removing duplicates
unique_indices = np.sort(unique_indices)
product_ids = product_ids[unique_indices]
product_names = product_names[unique_indices]
categories = categories[unique_indices]
price = price[unique_indices]
quantity = quantity[unique_indices]
rating = rating[unique_indices]
discount = discount[unique_indices]

# TASK 5: Vectorized Operations (Without Loops)

print("\nTask 5: Vectorized Operations")
revenue = price * quantity
Discounted_Price = price * (1 - discount/100)
Profit = revenue * 0.25
tax = revenue * 0.15
print("Vectorized calculations completed successfully.")

# TASK 6: Broadcasting
print("\nTask 6: Broadcasting")
multipliers = np.array([1.0, 1.1, 1.2, 0.9])
# Broadcasting to calculate projected revenue for different scenarios
projected_revenue = revenue[:, None] * multipliers
print("Projected Revenue Shape (N, 4):", projected_revenue.shape)

# TASK 7: Mathematical Analysis
revenue = price * quantity
revenue[revenue < 0] = 0
print("\nTask 7: Mathematical Analysis")
print("Total Revenue:", np.sum(revenue))
#replace with 0 if revenue == negative value
print("Average Revenue:", np.mean(revenue))
print("Max Revenue:", np.max(revenue))
print("Min Revenue:", np.min(revenue))
print("Revenue Standard Deviation:", np.std(revenue))

# Best selling and highest rated products
best_selling_prod = product_names[np.argmax(quantity)]
highest_rated_prod = product_names[np.argmax(rating)]
print("Best Selling Product:", best_selling_prod)
print("Highest Rated Product:", highest_rated_prod)