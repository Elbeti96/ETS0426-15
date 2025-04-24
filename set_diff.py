set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7}

set1.difference_update(set2, set3)
print(set1)  # Output: {1, 2}

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set1 -= set2
print(set1) # {1, 2}