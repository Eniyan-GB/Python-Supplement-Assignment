# Problem 60: Check if number is Armstrong number
# Find and fix the error

def is_armstrong(n):
    num_digits = len(str(n))
    return sum(int(d)**num_digits for d in str(n)) == n
