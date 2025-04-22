set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

set1.intersection_update(set2, set3)
print(set1)  # Output: {4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set1 &= set2
print(set1) #{3, 4, 5
