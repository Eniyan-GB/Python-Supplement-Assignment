# Problem 81: Check if string has balanced brackets
# Find and fix the error
def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:  # opening
            stack.append(char)
        elif char in pairs.values():  # closing
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack
