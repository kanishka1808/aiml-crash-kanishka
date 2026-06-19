# day5 task8-- Fraction Class using Dunder Methods

import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(
            self.numerator // gcd,
            self.denominator // gcd
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        den = self.denominator * other.denominator

        result = Fraction(num, den)
        return result.simplify()

    def __eq__(self, other):
        a = self.simplify()
        b = other.simplify()

        return (
            a.numerator == b.numerator
            and a.denominator == b.denominator
        )

    def __lt__(self, other):
        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )


# Test Cases

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print("Fraction 1:", f1)
print("Fraction 2:", f2)

print("Addition:", f1 + f2)

f3 = Fraction(2, 4)
f4 = Fraction(1, 2)

print("Equal?", f3 == f4)

f5 = Fraction(3, 5)
f6 = Fraction(4, 5)

print("Less Than?", f5 < f6)

# Explore Section
# @functools.total_ordering can automatically create
# comparison methods if __eq__ and one comparison
# method like __lt__ are defined.