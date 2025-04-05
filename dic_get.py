my_dict = {"name": "Alice", "age": 30}

name = my_dict.get("name")  # name will be "Alice"

city = my_dict.get("city")  # city will be None

city = my_dict.get("city", "Unknown")  # city will be "Unknown"

age = my_dict.get("age", 0)  # age will be 30 (key exists, default not used)
