##TASK 1

import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

print(customers)
print(products)
print(orders)

print(customers.shape)
print(products.shape)
print(orders.shape)

print(customers.columns)
print(products.columns)
print(orders.columns)

print(customers.dtypes)
print(products.dtypes)
print(orders.dtypes)

print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())



## Task 1: Data Audit

#The customers, products, and orders datasets were loaded and inspected.

#The Customers table contains 4 records and 4 columns.
#The Products table contains 4 records and 4 columns.
#The Orders table contains 5 records and 5 columns.

#No missing values were found in any table.
#No duplicate records were identified.
#The order_date column is currently stored as an object datatype and will be converted to datetime format during data cleaning.

#Overall, the data quality is good and suitable for further analysis.


##TASK 2
# Convert all column names to lowercase

customers.columns = customers.columns.str.lower()
products.columns = products.columns.str.lower()
orders.columns = orders.columns.str.lower()

print(customers.columns)
print(products.columns)
print(orders.columns)

print(orders.dtypes)

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

print(orders.dtypes)

print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())

customers_clean = customers.copy()
products_clean = products.copy()
orders_clean = orders.copy()


## Task 2: Data Cleaning

#The datasets were reviewed and cleaned before analysis.

#All column names were standardized to lowercase format to ensure consistency.

#The order_date column was converted from object datatype to datetime format, allowing time-based analysis.

#No missing values were found in any of the tables, therefore no imputation was required.

#No duplicate records were detected.

#Cleaned copies of the datasets were created and are ready for further analysis and merging.


## TASK 3
# Merge orders with customers

merged = pd.merge(
    orders_clean,
    customers_clean,
    on="customer_id"
)

print(merged)


merged = pd.merge(
    merged,
    products_clean,
    on="product_id"
)

print(merged)


merged["revenue"] = (
    merged["quantity"] *
    merged["price"]
)

print(
    merged[[
        "product_name",
        "quantity",
        "price",
        "revenue"
    ]]
)


category_sales = merged.groupby(
    "category"
)["revenue"].sum()

print(category_sales)


region_sales = merged.groupby(
    "region"
)["revenue"].sum()

print(region_sales)


segment_sales = merged.groupby(
    "segment"
)["revenue"].sum()

print(segment_sales)


multi_group = merged.groupby(
    ["region", "category"]
)["revenue"].sum()

print(multi_group)


## Task 3: GroupBy Analysis

#Sales performance was analyzed using Pandas groupby operations.

#Revenue was calculated using:

#Revenue = Quantity × Price

#Category-wise analysis shows that Electronics generated ₹140,000 in revenue, significantly higher than Furniture which generated ₹31,000.#Region-wise analysis indicates that the North region is the highest-performing region with ₹120,000 in revenue.

#Customer segment analysis reveals that the Consumer segment contributes the majority of sales revenue.

#A multi-level groupby was performed using Region and Category to understand how product categories perform within different regions.

#The analysis suggests that electronic products are the primary drivers of business revenue.


## TASK 4
total_revenue = merged["revenue"].sum()

print("Total Revenue =", total_revenue)


total_orders = merged["order_id"].nunique()

print("Total Orders =", total_orders)


aov = total_revenue / total_orders

print("Average Order Value =", aov)

product_revenue = merged.groupby(
    "product_name"
)["revenue"].sum()

print(product_revenue)


top_products = merged.groupby(
    "product_name"
)["revenue"].sum().sort_values(
    ascending=False
)

print(top_products)


top_quantity = merged.groupby(              
    "product_name"
)["quantity"].sum().sort_values(
    ascending=False
)

print(top_quantity)


print(merged.head())



## Task 4: Merging Tables and Key Metrics

#The Customers, Orders, and Products datasets were merged using customer_id and product_id.

#A new revenue column was created using the formula:

#Revenue = Quantity × Price

#Key business metrics were calculated from the merged dataset.

#Total Revenue generated across all orders is ₹171,000.

#The dataset contains 5 unique orders.

#The Average Order Value (AOV) is ₹34,200.

#Laptop is the highest revenue-generating product with ₹100,000 in sales revenue.

#Although Chair has the highest quantity sold, Laptop contributes the most revenue due to its higher price.

#The merged dataset provides a complete business view combining customer, product, and sales information.



pivot_region_category = pd.pivot_table(
    merged,
    values="revenue",
    index="region",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

print(pivot_region_category)


pivot_segment_category = pd.pivot_table(
    merged,
    values="revenue",
    index="segment",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

print(pivot_segment_category)


merged["month"] = merged["order_date"].dt.month_name()

print(
    merged[[
        "order_date",
        "month"
    ]]
)



pivot_month_category = pd.pivot_table(
    merged,
    values="revenue",
    index="month",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

print(pivot_month_category)


## Task 5: Pivot Table Analysis

#Pivot tables were created to analyze revenue across multiple dimensions.

#The first pivot table compared revenue across regions and product categories.

#The North region generated the highest Electronics revenue, while Furniture sales were concentrated in the East and West regions.

#The second pivot table compared customer segments and product categories.

#The Consumer segment contributed the highest overall revenue.

#An additional month-wise pivot table was created to understand revenue trends over time.

#Pivot tables provide a compact and readable summary of business performance and help identify patterns across multiple dimensions.


## TASK 6
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(6,4))

plt.hist(merged["revenue"])

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")

plt.show()


### Histogram Interpretation

#The histogram shows the distribution of revenue values across orders.

#Most orders fall within the lower revenue range, while a few orders generate significantly higher revenue.

plt.figure(figsize=(6,4))

plt.scatter(
    merged["quantity"],
    merged["revenue"]
)

plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")

plt.show()


### Scatter Plot Interpretation

#The scatter plot shows a positive relationship between quantity sold and revenue generated.

#Orders with larger quantities generally produce higher revenue.


category_sales = merged.groupby(
    "category"
)["revenue"].sum()

category_sales.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.show()


### Bar Chart Interpretation

#Electronics generates significantly higher revenue compared to Furniture.

#This indicates that electronic products are the major contributors to business revenue.


monthly_sales = merged.groupby(
    "month"
)["revenue"].sum()

monthly_sales.plot(kind="line")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()


### Line Chart Interpretation

#The line chart shows monthly revenue trends.

#January recorded the highest revenue due to strong electronic product sales.

plt.figure(figsize=(6,4))

sns.boxplot(
    x="category",
    y="revenue",
    data=merged
)

plt.title("Revenue Distribution by Category")

plt.show()


### Box Plot Interpretation

#The box plot highlights differences in revenue distribution between product categories.

#Electronics shows higher revenue values compared to Furniture.


pivot = pd.pivot_table(
    merged,
    values="revenue",
    index="region",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

sns.heatmap(
    pivot,
    annot=True
)

plt.title("Region vs Category Revenue")

plt.show()


### Heatmap Interpretation

#The heatmap clearly shows revenue concentration across regions and categories.

#North region dominates Electronics sales, while Furniture sales are concentrated in East and West regions.




## Task 6: Data Visualization

#Six different visualizations were created to explore sales performance and revenue patterns.

#The histogram revealed the distribution of revenue values.

#The scatter plot demonstrated the relationship between quantity sold and revenue generated.

#The bar chart highlighted category-wise revenue performance.

#The line chart showed monthly revenue trends.

#The box plot illustrated revenue variability across categories.

#The heatmap provided a comparative view of revenue across regions and categories.

#Together, these visualizations provide valuable business insights and support data-driven decision making.







## Task 7: Business Insights

#The visualizations show that Electronics is the highest-performing product category and contributes the majority of total revenue.

#Laptop sales alone generate ₹100,000 in revenue, making it the most valuable product in the dataset.

#The North region records the highest revenue due to strong Electronics sales.

#Although Chair has the highest quantity sold, it contributes less revenue because of its lower price compared to electronic products.

#Monthly revenue trends indicate that January was the strongest performing month.

#The Consumer segment contributes the highest share of overall revenue.

#Overall, the business appears to rely heavily on Electronics products for revenue generation and growth.




## TASK 8
import sqlite3

conn = sqlite3.connect("sales.db")

customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

query = """
SELECT
c.name,
SUM(quantity * price) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN products p
ON o.product_id = p.product_id
GROUP BY c.name
HAVING revenue >
(
    SELECT
    AVG(quantity * price)
    FROM orders o
    JOIN products p
    ON o.product_id = p.product_id
);
"""

result = pd.read_sql(query, conn)

print(result)

##SQL queries were used to retrieve, filter, sort, aggregate, and analyze business data. The analysis showed that Electronics is the highest revenue-generating category with ₹140,000 in sales. The North region contributes the highest revenue (₹120,000), and Laptop is the top-performing product. Customer-wise analysis revealed that Kanishka generated the highest revenue contribution of ₹120,000. SQL joins and aggregate functions helped uncover key business insights from the relational datasets.