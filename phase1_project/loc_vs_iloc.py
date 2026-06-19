# day7 task5 -- Compare .loc and .iloc on the Same Dataset


import pandas as pd

df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df)

print("\nUsing .loc")
print(df.loc[0:2, ["Name", "Score"]])

print("\nUsing .iloc")
print(df.iloc[0:3, [0, 3]])

print("\nDifference:")
print(".loc uses row/column labels")
print(".iloc uses row/column positions")