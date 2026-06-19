#day7 task4 -- Columns and Filter Rows from a DataFrame  

import pandas as pd

df = pd.read_csv("students.csv")

print(df.columns)



filtered = df[
    (df["Department"] == "AIML") &
    (df["Score"] > 80)
]

print("Selected Columns:")
print(filtered[["Name", "Score"]])

print("\nFilter Explanation:")
print("Department = AIML")
print("Score > 80")