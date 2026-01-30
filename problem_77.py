# Problem 77: Check if number is perfect square
# Find and fix the error

import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = math.isqrt(n)  # integer square root
    return sqrt * sqrt == n

print(f"Is 16 perfect square? {is_perfect_square(16)}")  # True
print(f"Is 15 perfect square? {is_perfect_square(15)}")  # False
