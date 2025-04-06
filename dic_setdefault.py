my_dict = {"name": "Alice", "age": 30}

name = my_dict.setdefault("name", "Bob")  # name will be "Alice" (key exists, dictionary unchanged)
print(my_dict) # Output: {"name": "Alice", "age": 30}

city = my_dict.setdefault("city", "New York")  # city will be "New York" (key created)
print(my_dict) #Output: {"name": "Alice", "age": 30, "city": "New York"}
