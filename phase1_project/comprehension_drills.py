# day5 task2-- This program demonstrates list comprehensions in Python.


# 1. Extract numbers divisible by 3

numbers = list(range(1, 21))
divisible_by_3 = [num for num in numbers if num % 3 == 0]

print("Numbers divisible by 3:")
print(divisible_by_3)

# 2. Words longer than 4 characters in title case

words = ["python", "code", "student", "book", "practice", "ai"]
long_words = [word.title() for word in words if len(word) > 4]

print("\nWords longer than 4 characters:")
print(long_words)

# 3. Convert Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("\nTemperatures in Fahrenheit:")
print(fahrenheit)

# 4. Flatten a nested list

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
flattened = [item for sublist in nested_list for item in sublist]

print("\nFlattened list:")
print(flattened)

# Explore: Dictionary Comprehension

squares = {x: x**2 for x in range(1, 6)}

print("\nDictionary Comprehension:")
print(squares)

# Explore: Set Comprehension

unique_lengths = {len(word) for word in words}

print("\nSet Comprehension:")
print(unique_lengths)