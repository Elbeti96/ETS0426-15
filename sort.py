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
