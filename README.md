# AI/ML Crash Course Practice Repository

This repository contains Python practice tasks completed during the AI/ML Crash Course.

---

# Day 3 Tasks

### intro.py

Basic Python introduction program.

Run:

```bash
python intro.py
```

### calculator.py

Performs basic arithmetic operations.

Run:

```bash
python calculator.py
```

### even_odd.py

Checks whether a number is even or odd.

Run:

```bash
python even_odd.py
```

### grade_classifier.py

Classifies grades based on marks.

Run:

```bash
python grade_classifier.py
```

### word_frequency.py

Counts the frequency of words in a text.

Run:

```bash
python word_frequency.py
```

### skills_counter.py

Performs counting and analysis on skills data.

Run:

```bash
python skills_counter.py
```

### tip_calculator.py

Calculates tip amount and total bill.

Run:

```bash
python tip_calculator.py
```

---

# Day 5 Tasks

## T1 - Student Report System

### student_report.py

Student report card system using OOP concepts.

Run:

```bash
python student_report.py
```

---

## T2 - List Comprehension Drills

### comprehension_drills.py

Practice exercises using list comprehensions.

Run:

```bash
python comprehension_drills.py
```

---

## T3 - File Records

### file_records.py

Reads student records from CSV and generates results.

### students.csv

Sample student records dataset.

### results.csv

Generated results containing averages and grades.

Run:

```bash
python file_records.py
```

---

## T4 - Typed Calculator

### typed_calculator.py

Calculator with type hints and docstrings.

Run:

```bash
python typed_calculator.py
```

---

## T5 - Library System

### library_system.py

Library management system using inheritance and method overriding.

Run:

```bash
python library_system.py
```

---

## T6 - JSON Config Manager

### config_manager.py

Save, load and update JSON configuration files.

### config.json

Generated configuration file.

Run:

```bash
python config_manager.py
```

---

## T7 - Pandas Dataset Exploration

### pandas_explore.py

Student dataset analysis using Pandas.

Run:

```bash
python pandas_explore.py
```

---

## T8 - Fraction Class

### fraction_class.py

Custom Fraction class using dunder methods.

Run:

```bash
python fraction_class.py
```

---

## T9 - Inventory Management System

### inventory.py

Inventory management system with CSV persistence.

### inventory.csv

Generated inventory data file.

Run:

```bash
python inventory.py
```

---

# Day 7 Tasks

## T1 - Student Profile Card using F-Strings and Type Hints

### profile_card.py

Builds a student profile card using Python F-Strings and Type Hints to create clean, structured, and readable output.

Run:

```bash
python profile_card.py
```

---

## T2 - Small Report from a JSON File

### json_report.py

Reads data from a JSON file and generates a formatted report by extracting and displaying relevant information.

### learner.json

Sample JSON data file used for report generation.

Run:

```bash
python json_report.py
```

---

## T3 - Demo Class with a Useful Method

### class_demo.py

Demonstrates the creation of a custom Python class with attributes and methods to showcase Object-Oriented Programming concepts.

Run:

```bash
python class_demo.py
```

---

## T4 - Columns and Filter Rows from a DataFrame

### filter_dataframe.py

Uses Pandas DataFrames to select specific columns and filter rows based on given conditions.

Run:

```bash
python filter_dataframe.py
```

---

## T5 - Compare .loc and .iloc on the Same Dataset

### loc_vs_iloc.py

Explores the differences between Pandas `.loc[]` and `.iloc[]` by performing row and column selection on the same dataset.

Run:

```bash
python loc_vs_iloc.py
```

---

## T6 - Clean Missing Values and Inspect the Dataset

### missing_values.py

Identifies, handles, and cleans missing values in a dataset while inspecting the data structure and quality.

Run:

```bash
python missing_values.py
```

---

## T7 - Produce Quick Insights with describe() and value_counts()

### insights.py

Generates summary statistics and category-wise insights using Pandas functions such as `describe()` and `value_counts()`.

Run:

```bash
python insights.py
```

---

## T8 - Build and Inspect NumPy Arrays, then Slice Them

### numpy_basics.py

Creates NumPy arrays, inspects their properties, and performs indexing and slicing operations.

Run:

```bash
python numpy_basics.py
```

---

## T9 - Use of Masking, Broadcasting, and a Similarity Calculation

### numpy_advanced.py

Demonstrates advanced NumPy concepts including masking, broadcasting, and similarity calculations for numerical data analysis.

Run:

```bash
python numpy_advanced.py
```

---

# Technologies Used for Day 3

* Python
* Variables and Data Types
* User Input
* Conditional Statements
* Arithmetic Operations
* Loops
* Functions
* String Manipulation
* Dictionaries

---


# Technologies Used for day5

* Python
* Pandas
* CSV Module
* JSON Module
* Object-Oriented Programming (OOP)
* File Handling
* Type Hints

---

# Technologies Used for day7

* Python
* NumPy
* Pandas
* JSON Module
* Object-Oriented Programming (OOP)
* Classes and Objects
* F-Strings
* Type Hints
* DataFrames
* Data Filtering
* Data Cleaning
* Missing Value Handling
* Dataset Inspection
* Statistical Analysis
* NumPy Array Operations
* Array Slicing and Indexing
* Masking and Broadcasting
* Similarity Calculations
* JSON Processing
* Report Generation

---


# ASSIGNMENT 1

# Sales Data Analysis Project

## Project Overview

This project demonstrates end-to-end data analysis using Python, Pandas, SQL, and data visualization techniques.

The analysis is performed on three datasets:

- Customers Data
- Products Data
- Orders Data

The objective of the project is to clean the data, perform exploratory analysis, generate business insights, visualize trends, and answer business questions using SQL queries.

---

## Project Files

### customers.csv
Contains customer information such as:

- Customer ID
- Customer Name
- Region
- Segment

### products.csv
Contains product information such as:

- Product ID
- Product Name
- Category
- Price

### orders.csv
Contains transaction details such as:

- Order ID
- Customer ID
- Product ID
- Quantity
- Order Date

### audit.py
Main Python script containing:

- Data Loading
- Data Auditing
- Data Cleaning
- GroupBy Analysis
- Revenue Calculations
- Pivot Tables
- Data Visualization
- SQLite Integration
- SQL Query Execution

### queries.sql
Contains SQL queries used for business analysis.

### sales.db
SQLite database created from the CSV files.

---

## Tasks Performed

### Task 1: Data Audit

Performed an initial audit of all datasets by checking:

- Dataset shape
- Column names
- Data types
- Missing values
- Summary statistics

---

### Task 2: Data Cleaning

Data cleaning steps included:

- Standardizing column names
- Converting date columns to proper datetime format
- Checking missing values
- Checking duplicate records

---

### Task 3: GroupBy Analysis

Used Pandas GroupBy operations to analyze:

- Revenue by Category
- Revenue by Region
- Revenue by Customer Segment
- Multi-level GroupBy Analysis

---

### Task 4: Business Metrics

Calculated key business metrics:

- Total Revenue
- Average Order Value (AOV)
- Product Revenue
- Top Selling Products

---

### Task 5: Pivot Table Analysis

Created pivot tables for:

- Region vs Category Revenue
- Segment vs Category Revenue
- Month vs Category Revenue

---

### Task 6: Data Visualization

Created multiple visualizations including:

- Histogram
- Scatter Plot
- Bar Chart
- Line Chart
- Box Plot
- Heatmap

These visualizations help identify trends and patterns in sales performance.

---

### Task 7: Business Insights

Key insights identified:

- Electronics is the highest revenue-generating category.
- Laptop is the top-performing product.
- North region generates the highest revenue.
- Consumer segment contributes the most revenue.
- January recorded the highest monthly revenue.

---

### Task 8: SQL Analysis

Created and executed SQL queries using SQLite.

Concepts covered:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- Aggregate Functions
- JOIN Operations
- Subqueries

SQL was used to answer important business questions and validate analysis results.

---

### Task 9: Pandas vs SQL Comparison

Compared the use of Pandas and SQL in data analysis workflows.

- SQL is efficient for querying structured databases.
- Pandas provides flexibility for data cleaning, transformation, analysis, and visualization.
- Both tools complement each other in real-world analytics projects.

---

## Technologies Used

- Python
- Pandas
- SQLite
- Matplotlib
- Seaborn
- VS Code

---

## Key Results

- Total Revenue: ₹171,000
- Average Order Value: ₹34,200
- Highest Revenue Category: Electronics
- Top Product: Laptop
- Highest Revenue Region: North
- Highest Revenue Segment: Consumer

---

## How to Run the Project

1. Place all CSV files in the project folder.
2. Open the project in VS Code.
3. Run the Python script:

```bash
python audit.py
```

4. Review the generated outputs, visualizations, and SQL query results.

---

## Conclusion

This project demonstrates a complete data analysis workflow including data auditing, cleaning, transformation, visualization, business intelligence reporting, and SQL-based analysis. The project highlights how Python and SQL can be used together to derive meaningful insights from business data.


---


# AI/ML Crash Course Practice Repository

## Assignment 2: Maths for Machine Learning and EDA

This assignment covers fundamental mathematical concepts used in Machine Learning along with Exploratory Data Analysis (EDA).

### Files

- `assignment2/housing_eda.py`
- `assignment2/maths_eda.py`

### Open Assignment

Go to the `assignment2` folder to view the complete documentation.


---


# Author

**Kanishka**

