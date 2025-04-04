# First commit
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
# Second commit
1. list.remove(element)

•  Explanation: The remove() method removes the first occurrence of a specified element from a list. It modifies the list directly. If the element is not found, it raises a ValueError.

•  Purpose: To delete a specific item from a list based on its value.

•  How it Works:

  1. The method takes a single element as input.
  2. It searches the list for the first occurrence of the element.
  3. If the element is found, it's removed from the list, and the remaining elements shift to fill the gap.
  4. If the element is not found, the method raises a ValueError.
  5. The list is modified in-place.

•  Important Notes:

  •  It removes only the first occurrence. To remove all occurrences, you might need a loop.
  •  Be prepared to handle the ValueError if the element is not guaranteed to be in the list.

•  Example (Python):
    my_list = [1, 2, 3, 2]
    my_list.remove(2)  # my_list will be [1, 3, 2] (first 2 removed)

    my_list = ["apple", "banana", "apple"]
    my_list.remove("apple") # my_list will be ["banana", "apple"]

    try:
        my_list.remove("grape") # This will raise a ValueError
    except ValueError:
        print("Element not found in the list")
2. list.pop([index])

•  Explanation: The pop() method removes and returns the element at a specified index in a list. If no index is specified, it removes and returns the last element. It modifies the list directly.

•  Purpose: To remove an element from a list and simultaneously retrieve its value.

•  How it Works:

  1. If an index is provided, the element at that index is removed from the list and returned.
  2. If no index is provided, the last element of the list is removed and returned.
  3. If the index is out of range, an IndexError is raised.
  4. The list is modified in-place.

•  Important Notes:

  •  Providing an index allows you to remove an element from a specific position.
  •  Calling pop() without an index is a common way to treat a list as a stack (Last-In, First-Out).

•  Example (Python):
    my_list = [1, 2, 3]
    popped_element = my_list.pop(1)  # my_list will be [1, 3], popped_element will be 2

    my_list = [1, 2, 3]
    last_element = my_list.pop()  # my_list will be [1, 2], last_element will be 3

    my_list = [1, 2, 3]
    try:
        element = my_list.pop(5) # This will cause an IndexError
    except IndexError:
        print("Index out of range")

3. list.clear()

•  Explanation: The clear() method removes all elements from a list, making it an empty list. It modifies the original list directly.

•  Purpose: To efficiently empty a list, removing all of its contents.

•  How it Works:

  1. The method iterates through the list.
  2. It removes each element from the list.
  3. The list becomes an empty list: [].
  4. The list is modified in-place.

•  Example (Python):
    my_list = [1, 2, 3]
    my_list.clear()  # my_list will be []
# Third commit 

1. list.copy()

•  Explanation: The copy() method creates a shallow copy of a list. This means it creates a new list with the same elements as the original list. Modifying the copy will not affect the original list, and vice versa (unless the list contains mutable objects).

•  Purpose: To create an independent copy of a list, allowing you to modify the copy without altering the original data.

•  How it Works:

  1. The method creates a new list object in memory.
  2. It iterates through the elements of the original list.
  3. It copies each element to the new list.
  4. The new list is returned.

•  Important Note: This is a shallow copy. If the list contains mutable objects (e.g., lists, dictionaries), changes to those objects within the copy will affect the original list (and vice-versa) because they both still reference the same underlying mutable objects. For a deep copy, use copy.deepcopy().

•  Example (Python):

    original_list = [1, 2, [3, 4]]
    copied_list = original_list.copy()

    copied_list[0] = 5  # Only modifies copied_list
    copied_list[2][0] = 6 # Modifies both lists

    print(original_list)  # Output: [1, 2, [6, 4]]
    print(copied_list)    # Output: [5, 2, [6, 4]]

2. list.reverse()

•   Explanation: The reverse() method reverses the order of elements in a list in place. It modifies the original list directly and does not return a new list.

•   Purpose: To efficiently reverse the order of elements in a list without creating a new list object.

•   How it Works:

    1.  The method iterates through the list, swapping the first element with the last, the second with the second-to-last, and so on, until it reaches the middle of the list.
    2.  The list is modified in-place.

•   Example (Python):

    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()  # my_list will be [5, 4, 3, 2, 1]

3. list.sort(key=None, reverse=False)

•  Explanation: The sort() method sorts the elements of a list in place. It modifies the original list directly. The sorting can be customized using the key and reverse arguments.

•  Purpose: To arrange the elements of a list in a specific order (ascending or descending).

•  How it Works:

  1. The method sorts the elements of the list based on their default comparison (usually numerical or alphabetical order).
  2. The key argument can be a function that takes an element as input and returns a value to use for sorting. This is useful for sorting based on a specific attribute of the elements.
  3. The reverse argument (a boolean) specifies whether to sort in ascending order (False, default) or descending order (True).
  4. The list is modified in-place.

•  Arguments:

  •  key (optional): A function that serves as a key for the sort comparison.
  •  reverse (optional): A boolean value. If True, the list is sorted in descending order.

•  Example (Python):

    my_list = [3, 1, 4, 1, 5, 9, 2, 6]
    my_list.sort()  # my_list will be [1, 1, 2, 3, 4, 5, 6, 9]

    my_list = ["banana", "apple", "cherry"]
    my_list.sort()  # my_list will be ["apple", "banana", "cherry"]

    my_list.sort(reverse=True) #Sorts in reverse order
    # my_list will be ['cherry', 'banana', 'apple']

    def get_length(item):
        return len(item)

    my_list = ["apple", "banana", "kiwi"]
    my_list.sort(key=get_length) # my_list will be ['kiwi', 'apple', 'banana']
# Fourth commit

1. list.index(element, start=0, end=None)

•  Explanation: The index() method returns the index (position) of the first occurrence of a specified element in the list. You can optionally specify a start and end index to limit the search to a specific portion of the list. If the element is not found, it raises a ValueError.

•  Purpose: To efficiently locate the position of a specific item in a list, with the option to restrict the search to a subset of the list.

•  How it Works:

  1. The method searches the list (or the specified slice of the list) from left to right for the element.
  2. If the element is found, the index of its first occurrence is returned.
  3. If the element is not found within the specified range (or the entire list), a ValueError is raised.

•  Arguments:

  •  element: The element to search for.
  •  start (optional): The index to start the search from (default is 0).
  •  end (optional): The index to end the search at (default is the end of the list). Note that the search will not include the element at the end index.

•  Example (Python):

    my_list = ["apple", "banana", "cherry", "apple"]
    index1 = my_list.index("banana")  # index1 will be 1

    index2 = my_list.index("apple", 1) # index2 will be 3 (starts search at index 1)

    try:
        index3 = my_list.index("grape") # Raises ValueError
    except ValueError:
        print("Element not found")

    try:
       index4 = my_list.index("apple", 1, 3) #Raises ValueError
    except ValueError:
      print("Element apple not found between index 1 and 3")

2. list.count(element)

•  Explanation: The count() method returns the number of times a specified element appears in the list.

•  Purpose: To determine how many times a particular value occurs in a list.

•  How it Works:

  1. The method iterates through the list.
  2. For each element in the list, it checks if it's equal to the element being searched for.
  3. It increments a counter for each match.
  4. The final count is returned.

•  Example (Python):


▌Important Considerations

•  The method returns the index of the first occurrence only.
•  A ValueError is raised if the element is not found.
•  The start and end arguments allow you to restrict the search to a specific portion of the list. Note that the end index isn't inclusive in search.

```

    my_list = [1, 2, 2, 3, 2, 4]
    count = my_list.count(2)  # count will be 3

    my_list = ["apple", "banana", "apple", "apple"]
    count2 = my_list.count("apple") # count2 will be 3

    count3 = my_list.count("grape") # count3 will be 0

3. list.__mul__(n) / list * n (List Multiplication)

•   Explanation: While not a traditional method called with dot notation, the __mul__ method (invoked via the * operator) allows you to multiply a list by an integer n. This creates a new list that contains n repetitions of the original list. The original list is not modified.

•   Purpose: To efficiently create a new list by repeating an existing list a specified number of times. Useful for initializing lists with repeating patterns or for creating data structures with a specific size and initial content.

•   How it Works:

    1.  The operator * is used with a list and an integer n.
    2.  The __mul__ method (behind the scenes) is invoked.
    3.  A new list is created.
    4. The elements of the original list are appended n times to the new list.
    5.  The new list is returned.

•   Important Notes:

    •   The original list is not modified.
    •   If n is 0, an empty list ([]) is returned.
    •   If n is negative, an empty list ([]) is returned.
    * The original elements themselves aren't copied, but reused. Modifications to a mutable element in the base list will be reflected in every repetition in the new list.

•   Example (Python):

    
    my_list = [1, 2, 3]
    repeated_list = my_list * 3  # repeated_list will be [1, 2, 3, 1, 2, 3, 1, 2, 3]

    empty_list = my_list * 0  # empty_list will be []

    negative_list = my_list * -2 # negative_list will be []

    list_with_mutable = [[1, 2], 3]
    repeated_mutable_list = list_with_mutable * 2
    repeated_mutable_list[0][0] = 5

    print(repeated_mutable_list) # [[5, 2], 3, [5, 2], 3]
    print(list_with_mutable) #[[5, 2], 3]
    