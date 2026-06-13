# day7 task8 -- Build and Inspect NumPy Arrays, then Slice Them  

import numpy as np

# Creating arrays
arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.arange(1, 11)

arr3 = np.zeros(5)

arr4 = np.linspace(0, 100, 5)

print("=== Array 1 ===")
print(arr1)

print("\n=== Array 2 ===")
print(arr2)

print("\n=== Array 3 ===")
print(arr3)

print("\n=== Array 4 ===")
print(arr4)

# Shape, dtype, ndim
print("\n=== Array Properties ===")

print("arr1 Shape:", arr1.shape)
print("arr1 Dtype:", arr1.dtype)
print("arr1 Dimensions:", arr1.ndim)

print("\narr2 Shape:", arr2.shape)
print("arr2 Dtype:", arr2.dtype)
print("arr2 Dimensions:", arr2.ndim)

# Negative Indexing
print("\n=== Negative Index ===")
print("Last element of arr1:", arr1[-1])

# Slicing
print("\n=== Slicing ===")
print("arr2[2:7] =", arr2[2:7])