my_dict = {"name": "Alice", "age": 30, "city": "New York"}

item = my_dict.popitem()  # item will be ("city", "New York") (in Python 3.7+)
print(my_dict) #my_dict is now {"name": "Alice", "age": 30}

try:
    empty_dict = {}
    empty_dict.popitem()  # Raises KeyError
except KeyError:
    print("Dictionary is empty")
