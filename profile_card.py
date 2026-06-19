# day7 task1-- a Student Profile Card using F-Strings and Type Hints 

from typing import Dict

student = {
    "name": "Kanishka",
    "course": "AI/ML",
    "city": "Jaipur"
}


def profile_card(data: Dict[str, str]) -> str:
    return (
        f"Student Name : {data['name']}\n"
        f"Course       : {data['course']}\n"
        f"City         : {data['city']}"
    )


print(profile_card(student))
