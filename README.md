# First commit
1. tuple.count(value)

•  Explanation: The count() method returns the number of times a specified value appears in the tuple.

•  Purpose: To determine how many times a particular element occurs within a tuple.

•  How it Works:

  1. The method iterates through the tuple.
  2. For each element in the tuple, it checks if it's equal to the value being searched for.
  3. It increments a counter for each match.
  4. The final count is returned.

•  Example (Python):

    my_tuple = (1, 2, 2, 3, 2, 4)
    count = my_tuple.count(2)  # count will be 3

    my_tuple = ("apple", "banana", "apple", "apple")
    count2 = my_tuple.count("apple")  # count2 will be 3

    count3 = my_tuple.count("grape")  # count3 will be 0

2. tuple.index(value, start=0, stop=sys.maxsize)

•  Explanation: The index() method returns the index of the first occurrence of a specified value in the tuple. You can optionally specify a start and stop index to limit the search to a specific portion of the tuple. If the value is not found, it raises a ValueError.

•  Purpose: To efficiently locate the position of a specific item in a tuple, with the option to restrict the search to a subset of the tuple.

•  How it Works:

  1. The method searches the tuple (or the specified slice of the tuple) from left to right for the value.
  2. If the value is found, the index of its first occurrence is returned.
  3. If the value is not found within the specified range (or the entire tuple), a ValueError is raised.

•  Arguments:

  •  value: The value to search for.
  •  start (optional): The index to start the search from (default is 0).
  •  stop (optional): The index to end the search at (default is the end of the tuple). Note that the search will not include the element at the stop index.

•  Example (Python):

    import sys
    my_tuple = ("apple", "banana", "cherry", "apple")
    index1 = my_tuple.index("banana")  # index1 will be 1

    index2 = my_tuple.index("apple", 1)  # index2 will be 3 (starts search at index 1)

    try:
        index3 = my_tuple.index("grape") # Raises ValueError
    except ValueError:
        print("Value not found")

    try:
       index4 = my_tuple.index("apple", 1, 3) #Raises ValueError
    except ValueError:
      print("Value apple not found between index 1 and 3")

3. Using Tuples with namedtuple

•  Explanation: While not a tuple method, the namedtuple factory function from the collections module allows you to create tuple-like objects with named fields. This enhances code readability and makes it easier to access elements by name instead of index.

•  Purpose: To create lightweight, immutable objects with named attributes, improving code clarity and maintainability.

•  How it Works:

  1. Import the namedtuple function from the collections module.
  2. Call namedtuple() with a name for the new class and a list of field names.
  3. The function returns a new class that is a subclass of tuple.
  4. Create instances of the class by passing values for the fields.
  5. Access tuple elements by either index or name

•  Example (Python):

    from collections import namedtuple

    # Create a namedtuple class
    Point = namedtuple("Point", ["x", "y"])

    # Create an instance of the Point class
    p = Point(10, 20)

    # Access elements by name
    print(p.x)  # Output: 10
    print(p.y)  # Output: 20

    # Access elements by index
    print(p[0])  # Output: 10
    print(p[1])  # Output: 20