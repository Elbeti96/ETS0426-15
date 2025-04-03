my_list = [1, 2, 3]
popped_element = my_list.pop(1)  # my_list will be [1, 3], popped_element will be 2

my_list = [1, 2, 3]
last_element = my_list.pop()  # my_list will be [1, 2], last_element will be 3

my_list = [1, 2, 3]
try:
    element = my_list.pop(5) # This will cause an IndexError
except IndexError:
    print("Index out of range")
