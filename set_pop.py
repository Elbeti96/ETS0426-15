my_set = {1, 2, 3}
element = my_set.pop()
print(f"Removed element: {element}")
print(f"Updated set: {my_set}")

try:
    empty_set = set()
    empty_set.pop()  # Raises KeyError
except KeyError:
    print("Set is empty")
