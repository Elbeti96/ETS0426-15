set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

difference_set = set1.difference(set2, set3)
print(difference_set)  # Output: {1, 2}

difference_set2 = set1 - set2 - set3
print(difference_set2) # {1, 2}

print(set1) # Original set not modified
