my_dict = {"name": "Alice", "age": 30}
update_dict = {"city": "New York", "age": 31}

my_dict.update(update_dict)  # my_dict is now {"name": "Alice", "age": 31, "city": "New York"}

my_dict.update([("gender", "Female"), ("occupation", "Engineer")]) #update with a list of tuples.

print(my_dict) # {'name': 'Alice', 'age': 31, 'city': 'New York', 'gender': 'Female', 'occupation': 'Engineer'}
