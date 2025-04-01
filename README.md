#First commit
1. list.append(element)

•   Explanation: The append() method adds a single element to the end of a list. It modifies the original list directly.

•   Purpose: To extend a list by adding a new item at the very end.

•   How it Works:

    1.  The method takes a single element as input.
    2.  It adds this element to the last position of the list.
    3.  The list is modified in-place; the method does not return a new list.
    4.  The element can be of any data type (number, string, list, dictionary, etc.).

•   Example (Python):
    my_list = [1, 2, 3]
    my_list.append(4)  # my_list will be [1, 2, 3, 4]

    my_list.append("hello") # my_list will be [1, 2, 3, 4, "hello"]

    my_list.append([5, 6]) # my_list will be [1, 2, 3, 4, "hello", [5, 6]]

2. list.extend(iterable)

•  Explanation: The extend() method adds all the elements of an iterable (like another list, tuple, or string) to the end of the list. It modifies the original list directly.

•  Purpose: To efficiently add multiple items from another collection to the end of a list.

•  How it Works:

  1. The method takes an iterable as input.
  2. It iterates through the iterable, adding each element to the end of the list.
  3. The list is modified in-place.
  4. The order of elements in the iterable is preserved when they are added to the list.

•  Example (Python):
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])  # my_list will be [1, 2, 3, 4, 5, 6]

    my_list.extend("hello") # my_list will be [1, 2, 3, 4, 5, 6, 'h', 'e', 'l', 'l', 'o']

    my_list.extend((7, 8)) # my_list will be [1, 2, 3, 4, 5, 6, 'h', 'e', 'l', 'l', 'o', 7, 8]

3. list.insert(index, element)

•  Explanation: The insert() method inserts an element at a specific index in a list. It modifies the original list by shifting existing elements to make space for the new element.

•  Purpose: To add a new item to a list at a chosen position.

•  How it Works:

  1. The method takes two arguments: index (the position where the element will be inserted) and element (the element to insert).
  2. It shifts all elements from the given index to the end of the list to the right by one position.
  3. It inserts the element at the specified index.
  4. The list is modified in-place.

•  Example (Python):
    my_list = [1, 2, 3]
    my_list.insert(1, "hello")  # my_list will be [1, "hello", 2, 3]

    my_list.insert(0, "start") # my_list will be ["start", 1, "hello", 2, 3]

    my_list.insert(len(my_list), "end") # my_list will be ["start", 1, "hello", 2, 3, "end"] (equivalent to append)