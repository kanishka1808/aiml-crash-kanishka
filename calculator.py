# Simple calculator program

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("add")
    print("subtract")
    print("multiply")
    print("divide")

    operation = input("Enter operation: ").lower()

    if operation in operations:

        result = operations[operation](num1, num2)

        print(f"\nResult: {result}")

    else:
        print("Invalid operation")


except ValueError:
    print("Please enter valid numbers")