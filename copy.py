original_list = [1, 2, [3, 4]]
copied_list = original_list.copy()

copied_list[0] = 5  # Only modifies copied_list
copied_list[2][0] = 6 # Modifies both lists

print(original_list)  # Output: [1, 2, [6, 4]]
print(copied_list)    # Output: [5, 2, [6, 4]]
