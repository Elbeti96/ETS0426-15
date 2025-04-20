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
# Second Commit
4. set.pop()

•  Explanation: The pop() method removes and returns an arbitrary element from the set. Because sets are unordered, you cannot predict which element will be removed. If the set is empty, calling pop() raises a KeyError.

•  Purpose: To remove and retrieve an element from a set when the specific element doesn't matter.

•  How it Works:

  1. If the set is empty, a KeyError is raised.
  2. Otherwise, an arbitrary element is removed from the set.
  3. The removed element is returned.

•  Arguments:

  •  None

•  Example (Python):

    my_set = {1, 2, 3}
    element = my_set.pop()
    print(f"Removed element: {element}")
    print(f"Updated set: {my_set}")

    try:
        empty_set = set()
        empty_set.pop()  # Raises KeyError
    except KeyError:
        print("Set is empty")

5. set.clear()

•  Explanation: The clear() method removes all elements from the set, making it an empty set. It modifies the original set directly.

•  Purpose: To efficiently empty a set, removing all of its contents.

•  How it Works:

  1. The method iterates through the set.
  2. It removes each element from the set.
  3. The set becomes an empty set: set().

•  Arguments:

  •  None

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.clear()
    print(my_set)  # Output: set()

6. set.copy()

•  Explanation: The copy() method creates a shallow copy of a set. This means that a new set object is created, but the elements themselves are references to the same objects as in the original set.

•  Purpose: To create a new set that is a copy of an existing set.

•  How it Works:

  1. A new set is created.
  2. For each element in the original set, a reference to that element is copied into the new set.

•  Important Notes:

  •  If the elements are immutable (e.g., numbers, strings, tuples), changes to the elements themselves will not affect the original set, and vice versa.
  •  If the elements are mutable (e.g., lists, dictionaries), changes to those mutable elements will affect both sets, because both sets are referencing the same mutable objects.
  •  To avoid this, use copy.deepcopy() from the copy module to create a deep copy if your set contains mutable elements.

•  Example (Python):

    import copy

    # Shallow copy
    original_set = {1, 2, [3, 4]}
    copied_set = original_set.copy()

    copied_set.remove([3, 4]) # remove the element so you can add it back in modified
    copied_set.add([5, 6]) #re-add it with the new element

    print(original_set)  # Output: {1, 2, [3, 4]}
    print(copied_set)    # Output: {1, 2, [5, 6]}

    # Deep copy (if you need it for mutable elements)
    original_set = {1, 2, [3, 4]}
    deep_copied_set = copy.deepcopy(original_set)

    deep_copied_set.remove([3, 4]) # remove the element so you can add it back in modified
    deep_copied_set.add([7, 8])

    print(original_set) # {1, 2, [3, 4]}
    print(deep_copied_set)  # {1, 2, [7, 8]}