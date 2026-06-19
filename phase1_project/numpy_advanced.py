# day7 task9 -- Use of Masking, Broadcasting, and a Similarity Calculation 

import numpy as np

# -----------------------------
# Masking
# -----------------------------

arr = np.array([5, 10, 15, 20, 25])

mask = arr > 10

print("=== Masking ===")
print("Original Array:", arr)
print("Values greater than 10:", arr[mask])

# -----------------------------
# Broadcasting
# -----------------------------

scaled_arr = arr * 2

print("\n=== Broadcasting ===")
print("Original Array:", arr)
print("After Multiplying by 2:", scaled_arr)

# -----------------------------
# Cosine Similarity
# -----------------------------

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)

    magnitude = (
        np.linalg.norm(v1)
        * np.linalg.norm(v2)
    )

    return dot_product / magnitude


vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

vector3 = np.array([1, 0, 0])
vector4 = np.array([0, 1, 0])

print("\n=== Cosine Similarity ===")

print(
    "Similarity between vector1 and vector2:",
    cosine_similarity(vector1, vector2)
)

print(
    "Similarity between vector3 and vector4:",
    cosine_similarity(vector3, vector4)
)