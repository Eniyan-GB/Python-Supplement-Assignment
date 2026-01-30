# Problem 19: Calculate power of a number
# Find and fix the error
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    else:  # negative exponent
        result = 1
        for _ in range(-exponent):
            result *= base
        return 1 / result

