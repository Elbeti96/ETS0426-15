my_dict = {"name": "Alice", "age": 30, "city": "New York"}

values_view = my_dict.values()

print(values_view)  # Output: dict_values(['Alice', 30, 'New York'])

my_dict["country"] = "USA"  # Add a new key-value pair

print(values_view)  # Output: dict_values(['Alice', 30, 'New York', 'USA']) (view is updated)

values_list = list(my_dict.values()) # get a static list

print(values_list) #['Alice', 30, 'New York', 'USA']
