my_list = [1, 2, 3, 2]
my_list.remove(2)  # my_list will be [1, 3, 2] (first 2 removed)

my_list = ["apple", "banana", "apple"]
my_list.remove("apple") # my_list will be ["banana", "apple"]

try:
    my_list.remove("grape") # This will raise a ValueError
except ValueError:
    print("Element not found in the list")
