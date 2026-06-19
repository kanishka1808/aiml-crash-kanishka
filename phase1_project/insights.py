#day7 task7 -- Produce Quick Insights with describe() and value_counts() 

import pandas as pd

df = pd.read_csv("students.csv")

print("=== Dataset ===")
print(df)

print("\n=== Describe Output ===")
print(df.describe())

print("\n=== Department Counts ===")
print(df["Department"].value_counts())

print("\n=== Insights ===")
print(f"Average Score: {df['Score'].mean():.2f}")
print("AIML is the most common department.")