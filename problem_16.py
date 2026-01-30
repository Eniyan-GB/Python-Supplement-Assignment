# Problem 16: Find the second largest number in a list
# Find and fix the error

numbers = [45, 89, 12, 78, 34]
largest = second = float('-inf')
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(f"Second largest: {second}")
