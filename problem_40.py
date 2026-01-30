# Problem 40: Count consonants in a string
# Find and fix the error

def count_consonants(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char.isalpha() and char not in vowels)


