# Problem 73: Find maximum difference between elements
# Find and fix the error

def max_difference(arr):
    # If fewer than 2 elements, no difference is possible
    if len(arr) < 2:
        return 0
    
    min_val = arr[0]       # smallest value seen so far
    max_diff = arr[1] - arr[0]  # start with first possible difference
    
    for i in range(1, len(arr)):
        diff = arr[i] - min_val
        if diff > max_diff:
            max_diff = diff
        if arr[i] < min_val:
            min_val = arr[i]
    
    return max_diff

numbers = [7, 1, 5, 3, 6, 4]
print(f"Max difference: {max_difference(numbers)}")  # Output: 5
