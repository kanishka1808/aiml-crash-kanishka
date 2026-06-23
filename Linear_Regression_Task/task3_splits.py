import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

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

# Different Test Sizes
test_sizes = [0.20, 0.30, 0.40]

results = []

for test_size in test_sizes:

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results.append([
        f"{int((1-test_size)*100)}/{int(test_size*100)}",
        mse,
        rmse,
        mae,
        r2
    ])

# Create DataFrame
comparison_df = pd.DataFrame(
    results,
    columns=[
        "Split",
        "MSE",
        "RMSE",
        "MAE",
        "R2"
    ]
)

print("\nTrain-Test Split Comparison\n")
print(comparison_df)

# Save Results
comparison_df.to_csv(
    "task3_split_comparison.csv",
    index=False
)

print("\nResults saved successfully!")



## Conclusion
 
# The Linear Regression model was evaluated using three train-test split ratios: 80/20, 70/30, and 60/40.
# Performance was measured using MSE, RMSE, MAE, and R² score.
# The 70/30 split achieved the lowest error values among all three configurations.
# The 70/30 split also achieved the highest R² score (0.6394).
# The 80/20 split produced slightly lower performance compared to the 70/30 split.
# The 60/40 split performed similarly to the 70/30 split but had slightly higher error values.
# Therefore, the 70/30 train-test split provided the most reliable and accurate predictions for this dataset.