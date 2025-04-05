my_dict = {"name": "Alice", "age": 30}

name = my_dict.pop("name")  # name will be "Alice", my_dict will be {"age": 30}

city = my_dict.pop("city", "Unknown")  # city will be "Unknown", my_dict remains {"age": 30}

try:
    gender = my_dict.pop("gender")  # Raises KeyError
except KeyError:
    print("Key 'gender' not found")
