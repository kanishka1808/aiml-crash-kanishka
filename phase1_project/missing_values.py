# day7 Task6  -- Clean Missing Values and Inspect the Dataset

import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    "Name": ["Kanishka", "Rahul", None, "Priya"],
    "Score": [88, np.nan, 75, 92]
}

df = pd.DataFrame(data)

print("=== Original Dataset ===")
print(df)

# Check missing values
print("\n=== Missing Values Count ===")
print(df.isnull().sum())

# fillna()
filled_df = df.fillna("Unknown")

print("\n=== After fillna() ===")
print(filled_df)

# dropna()
dropped_df = df.dropna()

print("\n=== After dropna() ===")
print(dropped_df)