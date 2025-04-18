my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

my_set.discard(4)  # No error is raised
print(my_set)  # Output: {1, 3}
