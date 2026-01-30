# Problem 56: Remove vowels from string
# Find and fix the error
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join([c for c in text if c not in vowels])
