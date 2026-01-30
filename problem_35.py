# Problem 35: Calculate percentage
# Find and fix the error

def calculate_percentage(obtained, total):
    return round((obtained / total) * 100, 2)

marks = 45
total_marks = 50
result = calculate_percentage(marks, total_marks)
print(f"Percentage: {result}%")
