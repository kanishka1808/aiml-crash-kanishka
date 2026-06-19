# day5 task3 --Student Records using CSV File I/O

import csv


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


# Step 1: Create students.csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "math", "science", "english"])

    writer.writerow(["Kanishka", 95, 90, 92])
    writer.writerow(["Rahul", 78, 80, 75])
    writer.writerow(["Priya", 60, 65, 58])


# Step 2: Read students.csv and calculate averages

results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        math = int(row["math"])
        science = int(row["science"])
        english = int(row["english"])

        average = (math + science + english) / 3
        grade = calculate_grade(average)

        results.append(
            {
                "name": row["name"],
                "average": round(average, 2),
                "grade": grade,
            }
        )


# Step 3: Create results.csv

with open("results.csv", "w", newline="") as file:
    fieldnames = ["name", "average", "grade"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(results)

print("students.csv created")
print("results.csv generated successfully")