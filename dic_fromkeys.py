keys = ["name", "age", "city"]
my_dict = dict.fromkeys(keys)  # my_dict will be {"name": None, "age": None, "city": None}

my_dict2 = dict.fromkeys(keys, "Unknown") # my_dict2 will be {"name": "Unknown", "age": "Unknown", "city": "Unknown"}

my_dict3 = dict.fromkeys("abc", 0) #my_dict3 will be {'a': 0, 'b': 0, 'c': 0}
