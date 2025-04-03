my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # my_list will be [1, 2, 3, 4, 5, 6]

my_list.extend("hello") # my_list will be [1, 2, 3, 4, 5, 6, 'h', 'e', 'l', 'l', 'o']

my_list.extend((7, 8)) # my_list will be [1, 2, 3, 4, 5, 6, 'h', 'e', 'l', 'l', 'o', 7, 8]
