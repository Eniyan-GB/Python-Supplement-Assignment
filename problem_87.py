# Problem 87: Generate Pascal's triangle
# Find and fix the error
def print_pascals_triangle(n):
    triangle = pascals_triangle(n)
    for row in triangle:
        print(' '.join(map(str, row)).center(n*2))

print_pascals_triangle(5)



