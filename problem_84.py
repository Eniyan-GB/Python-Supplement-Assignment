# Problem 84: Check if substring exists
# Find and fix the error

def contains_substring(text, substr):
    for i in range(len(text) - len(substr) + 1):
        if text[i:i+len(substr)] == substr:
            return True
    return False

sentence = "Python programming is fun"
print(contains_substring(sentence, "programming"))  # True
print(contains_substring(sentence, "Java"))         # False
