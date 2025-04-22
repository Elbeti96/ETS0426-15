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
# Third Commit
7. set.union(*others) or set | other | ...

•  Explanation: The union() method returns a new set containing all elements from the original set and all elements from the other set(s). The original sets are not modified. You can also use the | operator as a shorthand for union().

•  Purpose: To combine the elements of multiple sets into a single new set, eliminating duplicates.

•  How it Works:

  1. A new set is created.
  2. All elements from the original set are added to the new set.
  3. All elements from each of the other sets are added to the new set.
  4. Duplicate elements are automatically eliminated because sets only store unique values.
  5. The new set is returned.

•  Arguments:

  •  *others: One or more sets to combine with the original set.

•  Example (Python):

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = {5, 6, 7}

    union_set = set1.union(set2, set3)
    print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

    union_set2 = set1 | set2 | set3
    print(union_set2) # {1, 2, 3, 4, 5, 6, 7}

    print(set1) #Does not modify the original sets

8. set.intersection(*others) or set & other & ...

•  Explanation: The intersection() method returns a new set containing only the elements that are common to the original set and all of the other sets. You can also use the & operator as a shorthand for intersection().

•  Purpose: To find the common elements between multiple sets.

•  How it Works:

  1. A new set is created.
  2. The method iterates through the elements of the original set.
  3. For each element, it checks if that element is also present in all of the other sets.
  4. If the element is present in all sets, it is added to the new set.
  5. The new set is returned.

•  Arguments:

  •  *others: One or more sets to intersect with the original set.

•  Example (Python):

    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6}
    set3 = {4, 5, 6, 7}

    intersection_set = set1.intersection(set2, set3)
    print(intersection_set)  # Output: {4, 5}

    intersection_set2 = set1 & set2 & set3
    print(intersection_set2) # {4, 5}

    print(set1) #does not modify the original sets.

9. set.difference(*others) or set - other - ...

•  Explanation: The difference() method returns a new set containing the elements that are in the original set but not in any of the other sets. You can also use the - operator as a shorthand for difference().

•  Purpose: To find the elements that are unique to a set compared to other sets.

•  How it Works:

  1. A new set is created.
  2. The method iterates through the elements of the original set.
  3. For each element, it checks if that element is also present in any of the other sets.
  4. If the element is not present in any of the other sets, it is added to the new set.
  5. The new set is returned.

•  Arguments:

  •  *others: One or more sets to subtract from the original set.

•  Example (Python):

    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6}
    set3 = {4, 5, 6, 7}

    difference_set = set1.difference(set2, set3)
    print(difference_set)  # Output: {1, 2}

    difference_set2 = set1 - set2 - set3
    print(difference_set2) # {1, 2}

    print(set1) # Original set not modified
# Fourth commit
10. set.symmetric_difference(other) or set ^ other

•  Explanation: The symmetric_difference() method returns a new set containing the elements that are in either the original set or the other set, but not in both. It's the opposite of intersection. You can also use the ^ operator as a shorthand.

•  Purpose: To find the elements that are unique to either of two sets.

•  How it Works:

  1. A new set is created.
  2. The method iterates through the elements of the original set.
  3. If an element is not found in the other set, it's added to the new set.
  4. The method iterates through the elements of the other set.
  5. If an element is not found in the original set, it's added to the new set.
  6. The new set is returned.

•  Arguments:

  •  other: The other set.

•  Example (Python):

    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}

    symmetric_difference_set = set1.symmetric_difference(set2)
    print(symmetric_difference_set)  # Output: {1, 2, 6, 7}

    symmetric_difference_set2 = set1 ^ set2
    print(symmetric_difference_set2) # {1, 2, 6, 7}

    print(set1) # Original sets are not modified.

11. set.update(*others) or set |= other | ...

•  Explanation: The update() method modifies the original set by adding all the elements from the other set(s). This is an in-place operation. You can also use the |= operator as a shorthand.

•  Purpose: To efficiently add multiple elements from other sets into an existing set.

•  How it Works:

  1. The method iterates through the elements of each other set.
  2. For each element, it adds it to the original set.
  3. The original set is modified directly.

•  Arguments:

  •  *others: One or more sets to add to the original set.

•  Example (Python):

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = {5, 6, 7}

    set1.update(set2, set3)
    print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7}

    set4 = {8,9,10}
    set1 |= set4
    print(set1) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

12. set.intersection_update(*others) or set &= other & ...

•  Explanation: The intersection_update() method modifies the original set, keeping only the elements that are common to the original set and all of the other sets. You can also use the &= operator as a shorthand.

•  Purpose: To efficiently reduce a set to only the elements it shares with other sets.

•  How it Works:

  1. The method iterates through the elements of the original set.
  2. For each element, it checks if it is also present in all of the other sets.
  3. If the element is not present in all of the other sets, it is removed from the original set.
  4. The original set is modified directly.

•  Arguments:

  •  *others: One or more sets to intersect with the original set.

•  Example (Python):

    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6}
    set3 = {4, 5, 6, 7}

    set1.intersection_update(set2, set3)
    print(set1)  # Output: {4, 5}

    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6}
    set1 &= set2
    print(set1) #{3, 4, 5}