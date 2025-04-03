my_list = [1, 2, 3]
my_list.insert(1, "hello")  # my_list will be [1, "hello", 2, 3]

my_list.insert(0, "start") # my_list will be ["start", 1, "hello", 2, 3]

my_list.insert(len(my_list), "end") # my_list will be ["start", 1, "hello", 2, 3, "end"] (equivalent to append)
