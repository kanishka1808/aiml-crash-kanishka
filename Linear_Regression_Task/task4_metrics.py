import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    explained_variance_score
)

# Load Dataset
df = pd.read_csv("housing.csv")

# Handle Missing Values
df["total_bedrooms"] = df["total_bedrooms"].fillna(
    df["total_bedrooms"].median()
)

# One-Hot Encoding
df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)

# Features and Target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# -----------------------------
# SKLEARN METRICS
# -----------------------------

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nSKLEARN METRICS")
print("MSE :", mse)
print("RMSE:", rmse)
print("MAE :", mae)
print("R2  :", r2)

# -----------------------------
# MANUAL CALCULATIONS
# -----------------------------

mae_manual = np.mean(np.abs(y_test - y_pred))

mse_manual = np.mean((y_test - y_pred) ** 2)

rmse_manual = np.sqrt(mse_manual)

ss_res = np.sum((y_test - y_pred) ** 2)

ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)

r2_manual = 1 - (ss_res / ss_tot)

print("\nMANUAL METRICS")
print("MSE :", mse_manual)
print("RMSE:", rmse_manual)
print("MAE :", mae_manual)
print("R2  :", r2_manual)

# -----------------------------
# EXPLAINED VARIANCE SCORE
# -----------------------------

evs = explained_variance_score(
    y_test,
    y_pred
)

print("\nExplained Variance Score:")
print(evs)

# -----------------------------
# ARTIFICIAL ERROR EXPERIMENT
# -----------------------------

y_pred_modified = y_pred.copy()

y_pred_modified[:3] += 200000

mse_modified = mean_squared_error(
    y_test,
    y_pred_modified
)

rmse_modified = np.sqrt(
    mse_modified
)

mae_modified = mean_absolute_error(
    y_test,
    y_pred_modified
)

print("\nORIGINAL METRICS")
print("MSE :", mse)
print("RMSE:", rmse)
print("MAE :", mae)

print("\nMODIFIED METRICS")
print("MSE :", mse_modified)
print("RMSE:", rmse_modified)
print("MAE :", mae_modified)

# Save Comparison

comparison = pd.DataFrame({
    "Metric": ["MSE", "RMSE", "MAE"],
    "Original": [mse, rmse, mae],
    "Modified": [
        mse_modified,
        rmse_modified,
        mae_modified
    ]
})

comparison.to_csv(
    "task4_metric_comparison.csv",
    index=False
)

print("\nComparison file saved successfully!")
