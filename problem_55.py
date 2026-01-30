# Problem 55: Count frequency of each element
# Find and fix the error
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = Counter(numbers)
print(f"Frequency: {freq}")

