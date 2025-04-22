set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

set1.update(set2, set3)
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7}

set4 = {8,9,10}
set1 |= set4
print(set1) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
