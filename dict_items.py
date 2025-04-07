my_dict = {"name": "Alice", "age": 30, "city": "New York"}

keys_view = my_dict.keys()

print(keys_view)  # Output: dict_keys(['name', 'age', 'city'])

my_dict["country"] = "USA"  # Add a new key-value pair

print(keys_view)  # Output: dict_keys(['name', 'age', 'city', 'country']) (view is updated)
