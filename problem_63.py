# Problem 63: Find longest word in a sentence
# Find and fix the error

import string

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        clean_word = word.strip(string.punctuation)
        if len(clean_word) > len(longest):
            longest = clean_word
    return longest
