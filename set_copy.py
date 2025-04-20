import copy

# Shallow copy
original_set = {1, 2, [3, 4]}
copied_set = original_set.copy()

copied_set.remove([3, 4]) # remove the element so you can add it back in modified
copied_set.add([5, 6]) #re-add it with the new element

print(original_set)  # Output: {1, 2, [3, 4]}
print(copied_set)    # Output: {1, 2, [5, 6]}

# Deep copy (if you need it for mutable elements)
original_set = {1, 2, [3, 4]}
deep_copied_set = copy.deepcopy(original_set)

deep_copied_set.remove([3, 4]) # remove the element so you can add it back in modified
deep_copied_set.add([7, 8])

print(original_set) # {1, 2, [3, 4]}
print(deep_copied_set)  # {1, 2, [7, 8]}
