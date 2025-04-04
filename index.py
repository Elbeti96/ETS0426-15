my_list = ["apple", "banana", "cherry", "apple"]
index1 = my_list.index("banana")  # index1 will be 1

index2 = my_list.index("apple", 1) # index2 will be 3 (starts search at index 1)

try:
    index3 = my_list.index("grape") # Raises ValueError
except ValueError:
    print("Element not found")

try:
    index4 = my_list.index("apple", 1, 3) #Raises ValueError
except ValueError:
  print("Element apple not found between index 1 and 3")
