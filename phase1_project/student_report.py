# day5 task1 -- Student Report System using OOP

class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

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

    def __str__(self):
        return (
            f"School: {Student.school_name} | "
            f"Name: {self.name} | "
            f"Roll No: {self.roll_no} | "
            f"Average: {self.average():.2f} | "
            f"Grade: {self.grade()}"
        )


student1 = Student("Kanishka", 101, [95, 90, 92])
student2 = Student("Rahul", 102, [78, 80, 75])
student3 = Student("Priya", 103, [60, 65, 58])

print(student1)
print(student2)
print(student3)