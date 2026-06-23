# California Housing Price Prediction using Linear Regression

## Project Overview

This project applies Linear Regression on the California Housing Dataset to predict median house values. Different experiments were performed to evaluate model performance and understand the impact of features, train-test splits, and evaluation metrics.

## Dataset

* California Housing Dataset
* Total Records: 20,640
* Features: 10
* Target Variable: median_house_value

## Tasks Performed

### Task 1: Baseline Linear Regression Model

* Data preprocessing
* Missing value handling
* One-hot encoding
* Model training and testing
* Evaluation using MSE, RMSE, MAE, and R²

### Task 2: One Feature vs Multi Feature Comparison

* Single Feature: median_income
* Multiple Features: median_income, housing_median_age, total_rooms
* Performance comparison

### Task 3: Train-Test Split Comparison

* 80/20 Split
* 70/30 Split
* 60/40 Split
* Performance evaluation

### Task 4: Metric Verification

* Manual calculation of MAE, MSE, RMSE, and R²
* Comparison with Scikit-Learn metrics
* Error sensitivity analysis

## Results

* Baseline Model R² Score: 0.6254
* Best Train-Test Split: 70/30
* Multi-feature model outperformed the single-feature model.
* Manual metrics matched Scikit-Learn metrics exactly.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn




