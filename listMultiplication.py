my_list = [1, 2, 3]
repeated_list = my_list * 3  # repeated_list will be [1, 2, 3, 1, 2, 3, 1, 2, 3]

empty_list = my_list * 0  # empty_list will be []

negative_list = my_list * -2 # negative_list will be []

list_with_mutable = [[1, 2], 3]
repeated_mutable_list = list_with_mutable * 2
repeated_mutable_list[0][0] = 5

print(repeated_mutable_list) # [[5, 2], 3, [5, 2], 3]
print(list_with_mutable) #[[5, 2], 3]
    
