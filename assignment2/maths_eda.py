## TASK 1
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 + 2*x + 1

x = np.array([1, 3, 5])

h = 0.0001

derivative = (f(x + h) - f(x)) / h

print("Points:", x)
print("Derivative:", derivative)


x_curve = np.linspace(-2, 6, 200)

plt.figure(figsize=(8,5))

plt.plot(x_curve, f(x_curve), label="f(x)")

plt.scatter(x, f(x), color="red")

plt.title("Function Curve")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid(True)
plt.legend()

plt.show()


# Observations:
# 1. The graph is an upward-opening parabola.
# 2. The slope increases as x increases.
# 3. The derivative values at x=1, x=3, and x=5 are approximately 4, 8, and 12 respectively.



## TASK 2
print("\n--- Task 2: Gradient Descent ---")

x = 10

learning_rate = 0.1

for i in range(10):
    gradient = 2 * x
    x = x - learning_rate * gradient

    print(f"Iteration {i+1}: x = {x:.4f}")

    x = 10

learning_rate = 0.1

values = []

for i in range(10):
    values.append(x)
    gradient = 2 * x
    x = x - learning_rate * gradient

plt.figure(figsize=(8,5))

plt.plot(values, marker="o")

plt.title("Gradient Descent Convergence")
plt.xlabel("Iteration")
plt.ylabel("x value")

plt.grid(True)

plt.show()

# Observations:
# 1. The value of x decreases in every iteration.
# 2. Gradient Descent moves toward the minimum value.
# 3. The algorithm gradually converges toward x = 0.


## TASK 3
print("\n--- Task 3: Probability Basics ---")

import random

heads = 0
tails = 0

for i in range(1000):

    toss = random.choice(["H", "T"])

    if toss == "H":
        heads += 1
    else:
        tails += 1

print("Heads:", heads)
print("Tails:", tails)

print("Probability of Heads =", heads/1000)
print("Probability of Tails =", tails/1000)


plt.figure(figsize=(6,4))

plt.bar(["Heads", "Tails"], [heads, tails])

plt.title("Coin Toss Results")
plt.ylabel("Count")

plt.show()


# Observations:
# 1. Heads and tails occur almost equally often.
# 2. Experimental probability approaches theoretical probability.
# 3. As the number of tosses increases, the probability gets closer to 0.5.