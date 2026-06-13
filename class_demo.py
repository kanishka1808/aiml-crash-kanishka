# day7 task3 -- demo Class with a Useful Method

class Learner:

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def get_details(self):
        return f"{self.name} is learning {self.domain}"


student = Learner("Kanishka", "AI/ML")

print(student.get_details())