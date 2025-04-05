# First commit

1. dict.get(key, default=None)

•   Explanation: The get() method returns the value associated with a given key in a dictionary. If the key is present, its corresponding value is returned. If the key is not present, the method returns the specified default value (or None if no default is provided). This method provides a safe way to access dictionary values without risking a KeyError.

•   Purpose: To retrieve a value from a dictionary, providing a fallback if the key doesn't exist. This prevents your program from crashing due to a KeyError.

•   How it Works:

    1.  The method searches for the given key in the dictionary.
    2.  If the key is found, its corresponding value is returned.
    3.  If the key is not found:
        *   If a default value is specified, that value is returned.
        *   If no default value is specified, None is returned.

•   Arguments:

    •   key: The key to search for.
    •   default (optional): The value to return if the key is not found (defaults to None).

•   Example (Python):

    my_dict = {"name": "Alice", "age": 30}

    name = my_dict.get("name")  # name will be "Alice"

    city = my_dict.get("city")  # city will be None

    city = my_dict.get("city", "Unknown")  # city will be "Unknown"

    age = my_dict.get("age", 0)  # age will be 30 (key exists, default not used)

2. dict.pop(key, default=None)

•   Explanation: The pop() method removes the item with the specified key from the dictionary and returns its value. If the key is not found, and a default value is provided, it returns the default value. If the key is not found and no default value is provided, it raises a KeyError.

•   Purpose: To remove an item from a dictionary and simultaneously retrieve its value, providing a way to handle missing keys.

•   How it Works:

    1.  The method searches for the given key in the dictionary.
    2.  If the key is found:
        *   The item (key-value pair) is removed from the dictionary.
        *   The corresponding value is returned.
    3.  If the key is not found:
        *   If a default value is specified, that value is returned.
        *   If no default value is specified, a KeyError is raised.

•   Arguments:

    •   key: The key of the item to remove.
    •   default (optional): The value to return if the key is not found.

•   Example (Python):

    my_dict = {"name": "Alice", "age": 30}

    name = my_dict.pop("name")  # name will be "Alice", my_dict will be {"age": 30}

    city = my_dict.pop("city", "Unknown")  # city will be "Unknown", my_dict remains {"age": 30}

    try:
        gender = my_dict.pop("gender")  # Raises KeyError
    except KeyError:
        print("Key 'gender' not found")

3. dict.update(iterable or mapping)

•  Explanation: The update() method updates the dictionary with elements from another dictionary object or from an iterable of key/value pairs. Existing keys are overwritten; new keys are added.

•  Purpose: To merge the contents of one dictionary (or an iterable of key-value pairs) into another, efficiently updating the target dictionary.

•  How it Works:

  1. The method takes either a dictionary or an iterable (e.g., list of tuples) as input.
  2. It iterates through the key-value pairs in the input.
  3. For each key-value pair:
    *  If the key already exists in the dictionary, its value is updated.
    *  If the key does not exist, the new key-value pair is added to the dictionary.

•  Arguments:

  •  other_dict (or iterable): A dictionary or an iterable of key-value pairs.

•  Example (Python):

    my_dict = {"name": "Alice", "age": 30}
    update_dict = {"city": "New York", "age": 31}

    my_dict.update(update_dict)  # my_dict is now {"name": "Alice", "age": 31, "city": "New York"}

    my_dict.update([("gender", "Female"), ("occupation", "Engineer")]) #update with a list of tuples.

    print(my_dict) # {'name': 'Alice', 'age': 31, 'city': 'New York', 'gender': 'Female', 'occupation': 'Engineer'}