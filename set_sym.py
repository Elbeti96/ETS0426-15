set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 6, 7}

symmetric_difference_set2 = set1 ^ set2
print(symmetric_difference_set2) # {1, 2, 6, 7}

print(set1) # Original sets are not modified.
