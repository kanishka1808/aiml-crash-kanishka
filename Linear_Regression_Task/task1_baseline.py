import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load Dataset
df = pd.read_csv("housing.csv")

# Check dataset
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df["total_bedrooms"] = df["total_bedrooms"].fillna(
    df["total_bedrooms"].median()
)

# Convert categorical column
df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)

# Features and Target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Train-Test Split (80-20)
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

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n----- Model Performance -----")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAE  : {mae:.2f}")
print(f"R²   : {r2:.4f}")

# Actual vs Predicted Table
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\n----- First 10 Rows -----")
print(results.head(10))

# Save first 10 rows
results.head(10).to_csv(
    "actual_vs_predicted.csv",
    index=False
)

# Plot
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred)

plt.xlabel("Actual House Value")
plt.ylabel("Predicted House Value")
plt.title("Actual vs Predicted Values")

plt.tight_layout()

plt.savefig("actual_vs_predicted_plot.png")

plt.show()

print("\nGraph saved successfully!")
print("Table saved successfully!")


# A baseline Linear Regression model was developed to predict median house values using the California Housing dataset. The model achieved an R² score of 0.6254, indicating that it explained approximately 62.54% of the variance in house prices. The RMSE and MAE values suggest moderate prediction accuracy. The Actual vs Predicted plot showed a positive relationship between true and predicted values, confirming that the model captured the overall trend of the data.