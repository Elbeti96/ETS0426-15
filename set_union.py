set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

union_set = set1.union(set2, set3)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

union_set2 = set1 | set2 | set3
print(union_set2) # {1, 2, 3, 4, 5, 6, 7}

print(set1) #Does not modify the original sets
