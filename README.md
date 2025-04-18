# First commit

1. set.add(element)

•  Explanation: The add() method adds a single element to the set. If the element is already present in the set, the set remains unchanged (sets do not allow duplicate elements).

•  Purpose: To add a new element to a set, ensuring uniqueness.

•  How it Works:

  1. The method checks if the element is already present in the set.
  2. If the element is not present, it is added to the set.
  3. If the element is already present, the set remains unchanged.

•  Arguments:

  •  element: The element to add to the set.

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)  # Output: {1, 2, 3, 4}

    my_set.add(2)  # Adding an existing element has no effect
    print(my_set)  # Output: {1, 2, 3, 4}

2. set.remove(element)

•  Explanation: The remove() method removes a specified element from the set. If the element is not found in the set, it raises a KeyError.

•  Purpose: To remove a specific element from a set.

•  How it Works:

  1. The method checks if the element is present in the set.
  2. If the element is present, it is removed.
  3. If the element is not present, a KeyError is raised.

•  Arguments:

  •  element: The element to remove.

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)  # Output: {1, 3}

    try:
        my_set.remove(4)  # Raises KeyError
    except KeyError:
        print("Element not found")

3. set.discard(element)

•  Explanation: The discard() method removes a specified element from the set if it is present. Unlike remove(), it does not raise an error if the element is not found; it simply does nothing.

•  Purpose: To remove an element from a set without worrying about whether it exists. This provides a safer way to remove elements compared to remove().

•  How it Works:

  1. The method checks if the element is present in the set.
  2. If the element is present, it is removed.
  3. If the element is not present, the set remains unchanged.

•  Arguments:

  •  element: The element to remove.

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.discard(2)
    print(my_set)  # Output: {1, 3}

    my_set.discard(4)  # No error is raised
    print(my_set)  # Output: {1, 3}