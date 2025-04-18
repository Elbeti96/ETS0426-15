my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

try:
    my_set.remove(4)  # Raises KeyError
except KeyError:
    print("Element not found")
