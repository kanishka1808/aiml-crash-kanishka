# day5 task4 -- Calculator with Type Hints

from typing import Optional


def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """Returns the quotient of two numbers. Returns None if divisor is zero."""
    if b == 0:
        return None
    return a / b


def power(base: float, exp: float) -> float:
    """Returns base raised to the given exponent."""
    return base ** exp


def modulo(a: int, b: int) -> Optional[int]:
    """Returns the remainder. Returns None if divisor is zero."""
    if b == 0:
        return None
    return a % b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))