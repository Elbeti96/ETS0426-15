import copy

# Shallow copy
original_dict = {"name": "Alice", "age": 30, "address": ["123 Main St"]}
copied_dict = original_dict.copy()

copied_dict["name"] = "Bob"  # Only affects copied_dict
copied_dict["address"][0] = "456 Oak Ave"  # Affects BOTH dictionaries!

print(original_dict)  # Output: {'name': 'Alice', 'age': 30, 'address': ['456 Oak Ave']}
print(copied_dict)    # Output: {'name': 'Bob', 'age': 30, 'address': ['456 Oak Ave']}

# Deep copy
original_dict = {"name": "Alice", "age": 30, "address": ["123 Main St"]}
deep_copied_dict = copy.deepcopy(original_dict)

deep_copied_dict["address"][0] = "789 Pine Ln"  # Only affects deep_copied_dict

print(original_dict) # {'name': 'Alice', 'age': 30, 'address': ['123 Main St']}
print(deep_copied_dict)  # {'name': 'Alice', 'age': 30, 'address': ['789 Pine Ln']}
