# Problem 64: Merge two sorted lists
# Find and fix the error
def merge_sorted(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # Append remaining elements
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.ap

