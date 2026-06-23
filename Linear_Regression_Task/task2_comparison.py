import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load data
df = pd.read_csv("housing.csv")

# Missing values
df["total_bedrooms"] = df["total_bedrooms"].fillna(
    df["total_bedrooms"].median()
)

# -------------------
# MODEL A
# One Feature
# -------------------

X1 = df[["median_income"]]
y = df["median_house_value"]

X_train, X_test, y_train, y_test = train_test_split(
    X1,
    y,
    test_size=0.20,
    random_state=42
)

model1 = LinearRegression()
model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)

mse1 = mean_squared_error(y_test, pred1)
rmse1 = mse1 ** 0.5
mae1 = mean_absolute_error(y_test, pred1)
r21 = r2_score(y_test, pred1)

# -------------------
# MODEL B
# Multiple Features
# -------------------

X2 = df[
    [
        "median_income",
        "housing_median_age",
        "total_rooms"
    ]
]

X_train, X_test, y_train, y_test = train_test_split(
    X2,
    y,
    test_size=0.20,
    random_state=42
)

model2 = LinearRegression()
model2.fit(X_train, y_train)

pred2 = model2.predict(X_test)

mse2 = mean_squared_error(y_test, pred2)
rmse2 = mse2 ** 0.5
mae2 = mean_absolute_error(y_test, pred2)
r22 = r2_score(y_test, pred2)

# Comparison Table

comparison = pd.DataFrame({
    "Model": [
        "One Feature",
        "Multiple Features"
    ],
    "MSE": [
        mse1,
        mse2
    ],
    "RMSE": [
        rmse1,
        rmse2
    ],
    "MAE": [
        mae1,
        mae2
    ],
    "R2": [
        r21,
        r22
    ]
})

print("\nComparison Table\n")
print(comparison)

comparison.to_csv(
    "task2_comparison_results.csv",
    index=False
)

print("\nResults saved successfully!")



## conclusion

# Model A was built using only one feature: median_income.
# Model B was built using three features: median_income, housing_median_age, and total_rooms.
# Both models were trained and evaluated using the same train-test split.
# The multi-feature model produced lower MSE, RMSE, and MAE values than the one-feature model.
# The multi-feature model achieved a higher R² score.
# Lower error values indicate better prediction accuracy.
# A higher R² score indicates that the model explains more variance in the target variable.
# Therefore, the multi-feature model performed better than the one-feature model.
# The improved performance is due to the use of additional relevant features, which provided more information for predicting house prices.