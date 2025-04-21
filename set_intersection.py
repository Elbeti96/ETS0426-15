set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

intersection_set = set1.intersection(set2, set3)
print(intersection_set)  # Output: {4, 5}

intersection_set2 = set1 & set2 & set3
print(intersection_set2) # {4, 5}

print(set1) #does not modify the original sets.
