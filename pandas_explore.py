# day5 task7 -- Exploring Student Data using Pandas

import pandas as pd

# Creating DataFrame
data = {
    "name": [
        "Kanishka", "Rahul", "Priya", "Aman", "Neha",
        "Riya", "Arjun", "Simran", "Kabir", "Anjali"
    ],
    "city": [
        "Delhi", "Mumbai", "Delhi", "Pune", "Mumbai",
        "Pune", "Delhi", "Mumbai", "Pune", "Delhi"
    ],
    "math_score": [95, 78, 85, 67, 92, 74, 88, 81, 69, 90],
    "science_score": [90, 80, 82, 70, 95, 76, 85, 84, 72, 91],
    "english_score": [92, 75, 88, 65, 89, 79, 87, 80, 70, 93]
}

df = pd.DataFrame(data)

# 1. Average score in each subject
print("Average Scores:")
print(df[["math_score", "science_score", "english_score"]].mean())

# 2. Student with highest total score
df["total_score"] = (
    df["math_score"]
    + df["science_score"]
    + df["english_score"]
)

top_student = df.loc[df["total_score"].idxmax()]

print("\nTop Student:")
print(top_student[["name", "total_score"]])

# 3. Number of students from each city
print("\nStudents per City:")
print(df["city"].value_counts())

# 4. Students with math score above 75
print("\nMath Score Above 75:")
print(df[df["math_score"] > 75])

# Explore Section - Top 3 Students
print("\nTop 3 Students:")
print(df.nlargest(3, "total_score")[["name", "total_score"]])