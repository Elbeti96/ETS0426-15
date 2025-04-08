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
# Second commit

1. dict.setdefault(key, default)

•   Explanation: The setdefault() method returns the value associated with a given key in a dictionary. However, if the key is not present, it inserts the key with the specified default value into the dictionary and returns the default value. This method provides a concise way to retrieve a value or initialize it if it doesn't exist.

•   Purpose: To retrieve a dictionary value efficiently, and, if it doesn't exist, create it with a default value in a single operation.

•   How it Works:

    1.  The method searches for the given key in the dictionary.
    2.  If the key is found, its corresponding value is returned (and the dictionary is not modified).
    3.  If the key is not found:
        *   The key is inserted into the dictionary with the specified default value.
        *   The default value is returned.

•   Arguments:

    •   key: The key to search for or insert.
    •   default: The value to return and insert if the key is not found.

•   Example (Python):

    my_dict = {"name": "Alice", "age": 30}

    name = my_dict.setdefault("name", "Bob")  # name will be "Alice" (key exists, dictionary unchanged)
    print(my_dict) # Output: {"name": "Alice", "age": 30}

    city = my_dict.setdefault("city", "New York")  # city will be "New York" (key created)
    print(my_dict) #Output: {"name": "Alice", "age": 30, "city": "New York"}

2. dict.popitem()

•  Explanation: The popitem() method removes and returns an arbitrary (key, value) pair from the dictionary. In versions of Python before 3.7, the pair was removed in a relatively unpredictable order. In Python 3.7 and later, popitem() removes the last inserted key-value pair. If the dictionary is empty, calling popitem() raises a KeyError.

•  Purpose: To remove and retrieve a dictionary item when the specific key doesn't matter, often used in scenarios where you're iterating and consuming the dictionary.

•  How it Works:

  1. If the dictionary is empty, a KeyError is raised.
  2. Otherwise, a (key, value) pair is removed. In Python 3.7+, this will be the last inserted pair.
  3. The removed (key, value) pair is returned as a tuple.

•  Arguments:

  •  None

•  Example (Python):

    my_dict = {"name": "Alice", "age": 30, "city": "New York"}

    item = my_dict.popitem()  # item will be ("city", "New York") (in Python 3.7+)
    print(my_dict) #my_dict is now {"name": "Alice", "age": 30}

    try:
        empty_dict = {}
        empty_dict.popitem()  # Raises KeyError
    except KeyError:
        print("Dictionary is empty")

3. dict.fromkeys(seq, value=None)

•  Explanation: The fromkeys() method creates a new dictionary with keys from seq (an iterable like a list or tuple) and values set to value (which defaults to None). It's a class method, so it's called on the dict class itself, not on a dictionary instance.

•  Purpose: To efficiently create a dictionary with a predefined set of keys and a common initial value.

•  How it Works:

  1. The method takes an iterable seq as input, which will be used to create the keys of the new dictionary.
  2. It takes an optional value argument, which will be assigned as the value for all keys. If omitted, the value will be None.
  3. A new dictionary is created.
  4. The new dictionary is returned

•  Arguments:

  •  seq: An iterable (e.g., list, tuple, string, set) that will be used to create the keys of the new dictionary.
  •  value (optional): The value to assign to all keys (defaults to None).

•  Example (Python):

    keys = ["name", "age", "city"]
    my_dict = dict.fromkeys(keys)  # my_dict will be {"name": None, "age": None, "city": None}

    my_dict2 = dict.fromkeys(keys, "Unknown") # my_dict2 will be {"name": "Unknown", "age": "Unknown", "city": "Unknown"}

    my_dict3 = dict.fromkeys("abc", 0) #my_dict3 will be {'a': 0, 'b': 0, 'c': 0}
# Third Commit

1. dict.values()

•  Explanation: The values() method returns a view object that displays a list of all the values in the dictionary. This view object is dynamic, meaning that if you change the dictionary, the view object will reflect those changes. The order of the values in the view object is guaranteed to match the insertion order in Python 3.7+.

•  Purpose: To efficiently access and iterate over the values in a dictionary.

•  How it Works:

  1. The method creates a view object that represents the dictionary's values.
  2. The view object provides a dynamic view of the values, reflecting any changes made to the dictionary.
  3. The order of the values corresponds to the insertion order (Python 3.7+).

•  Important Notes:

  •  The returned object is a view, not a static list.
  •  Changes to the dictionary are immediately reflected in the view.
  •  To get a static list of the values, you can use list(dict.values()).
  •  The order of values is guaranteed to match insertion order in Python 3.7+.

•  Example (Python):

    my_dict = {"name": "Alice", "age": 30, "city": "New York"}

    values_view = my_dict.values()

    print(values_view)  # Output: dict_values(['Alice', 30, 'New York'])

    my_dict["country"] = "USA"  # Add a new key-value pair

    print(values_view)  # Output: dict_values(['Alice', 30, 'New York', 'USA']) (view is updated)

    values_list = list(my_dict.values()) # get a static list

    print(values_list) #['Alice', 30, 'New York', 'USA']

2. dict.items()

•  Explanation: The items() method returns a view object that displays a list of a dictionary's key-value pairs (items) as tuples. This view object is dynamic, meaning that if you change the dictionary, the view object will reflect those changes. The order of the items is guaranteed to match the insertion order in Python 3.7+.

•  Purpose: To efficiently iterate over both keys and values in a dictionary simultaneously.

•  How it Works:

  1. The method creates a view object that represents the dictionary's items.
  2. Each item is represented as a tuple (key, value).
  3. The view object provides a dynamic view, reflecting any changes made to the dictionary.
  4. The order of the items is guaranteed to match the insertion order in Python 3.7+.

•  Important Notes:

  •  The returned object is a view, not a static list.
  •  Changes to the dictionary are immediately reflected in the view.
  •  To get a static list of the items, you can use list(dict.items()).
  * You can unpack the view into key, value pairs.
  •  The order of values is guaranteed to match the insertion order in Python 3.7+.

•  Example (Python):

    my_dict = {"name": "Alice", "age": 30, "city": "New York"}

    items_view = my_dict.items()

    print(items_view)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

    my_dict["country"] = "USA"

    print(items_view)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York'), ('country', 'USA')])

    for key, value in items_view:
      print(f"{key}: {value}")

3. dict.keys()

•  Explanation: The keys() method returns a view object that displays a list of all the keys in the dictionary. This view object is dynamic, meaning that if you change the dictionary, the view object will reflect those changes. The order of the keys in the view object is guaranteed to match the insertion order in Python 3.7+.

•  Purpose: To efficiently access and iterate over the keys in a dictionary.

•  How it Works:

  1. The method creates a view object that represents the dictionary's keys.
  2. The view object provides a dynamic view of the keys, reflecting any changes made to the dictionary.
  3. The order of the keys corresponds to the insertion order (Python 3.7+).

•  Important Notes:

  •  The returned object is a view, not a static list.
  •  Changes to the dictionary are immediately reflected in the view.
  •  To get a static list of the keys, you can use list(dict.keys()).
  •  The order of keys is guaranteed to match the insertion order in Python 3.7+.

•  Example (Python):

    my_dict = {"name": "Alice", "age": 30, "city": "New York"}

    keys_view = my_dict.keys()

    print(keys_view)  # Output: dict_keys(['name', 'age', 'city'])

    my_dict["country"] = "USA"  # Add a new key-value pair

    print(keys_view)  # Output: dict_keys(['name', 'age', 'city', 'country']) (view is updated)
# Fourth commit

1. dict.clear() (Revisited with timing)

•  Explanation: The clear() method removes all items from the dictionary, making it an empty dictionary ({}). It modifies the original dictionary directly. It is typically used for memory management but can be slower for very large dictionaries.

•  Purpose: To efficiently empty a dictionary, removing all of its contents. However, it's important to be aware of potential performance implications for very large dictionaries.

•  How it Works:

  1. The method iterates through the dictionary.
  2. It removes each key-value pair from the dictionary.
  3. The dictionary becomes an empty dictionary: {}.
  4. The list is modified in-place.

•  Important Notes:

  •  The dictionary is modified in-place.

•  Example (Python):

    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    my_dict.clear()
    print(my_dict)  # Output: {}

2. dict.__contains__(key) or key in dict (Checking Key Existence)

•  Explanation: While not a typical method call with dot notation, the __contains__ method (invoked via the in operator) checks if a specific key exists in the dictionary.

•  Purpose: To efficiently determine whether a key is present in a dictionary.

•  How it Works:

  1. The in operator is used with a key and a dictionary.
  2. The __contains__ method (behind the scenes) is invoked.
  3. If the key exists in the dictionary, it returns True; otherwise, it returns False.

•  Important Notes:

  * This method only checks for the existence of the key, not the value.

•  Example (Python):

?, [4/8/2025 2:08 PM]
    my_dict = {"name": "Alice", "age": 30}
    has_name = "name" in my_dict  # has_name will be True
    has_city = "city" in my_dict  # has_city will be False

3. dict.copy() (Revisited and Expanded)

•  Explanation: The copy() method creates a shallow copy of a dictionary. This means a new dictionary object is created, but the keys and values themselves are references to the same objects as in the original dictionary. This has important implications when the values are mutable.

•  Purpose: To create a copy of a dictionary while understanding the difference between shallow and deep copies, especially when dealing with mutable values.

•  How it Works:

  1. A new dictionary is created.
  2. For each key-value pair in the original dictionary, a reference to the key and a reference to the value are copied into the new dictionary.

•  Important Notes:

  •  If the values are immutable (e.g., numbers, strings, tuples), changes to the values in the copy will not affect the original dictionary, and vice versa.
  •  If the values are mutable (e.g., lists, dictionaries), changes to those values in the copy will affect the original dictionary, and vice versa, because both dictionaries are referencing the same mutable objects.
  •  To avoid this, use copy.deepcopy() from the copy module to create a deep copy, where all objects are copied recursively.

•  Example (Python):

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