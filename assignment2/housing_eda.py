import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()

df = pd.DataFrame(
    housing.data,
    columns=housing.feature_names
)

df["Price"] = housing.target

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

plt.figure(figsize=(8,5))

plt.hist(df["Price"], bins=30)

plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

# Observation:
# Most house prices are concentrated in the lower and middle price ranges.
# Very high-priced houses are comparatively fewer.


plt.figure(figsize=(8,5))

plt.scatter(df["MedInc"], df["Price"])

plt.title("Median Income vs House Price")
plt.xlabel("Median Income")
plt.ylabel("House Price")

plt.show()

# Observation:
# Higher median income generally corresponds to higher house prices.
# A positive relationship exists between income and price.

plt.figure(figsize=(10,8))

sns.heatmap(df.corr(), annot=True)

plt.title("Correlation Heatmap")

plt.show()

# Observation:
# Median Income (MedInc) has the strongest positive correlation with Price.
# Some variables have weak correlations with Price.


# Final Insights:
#
# 1. The dataset contains 20640 records and 9 numerical features.
#
# 2. No missing values were found in the dataset.
#
# 3. House prices are mostly concentrated in lower and middle ranges.
#
# 4. Median Income has a strong positive relationship with house prices.
#
# 5. Correlation analysis shows that income is one of the most important
#    factors influencing housing prices.
#
# 6. The dataset is suitable for machine learning and predictive modeling.