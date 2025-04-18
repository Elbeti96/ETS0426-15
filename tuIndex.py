import sys
my_tuple = ("apple", "banana", "cherry", "apple")
index1 = my_tuple.index("banana")  # index1 will be 1

index2 = my_tuple.index("apple", 1)  # index2 will be 3 (starts search at index 1)

try:
    index3 = my_tuple.index("grape") # Raises ValueError
except ValueError:
    print("Value not found")

try:
   index4 = my_tuple.index("apple", 1, 3) #Raises ValueError
except ValueError:
  print("Value apple not found between index 1 and 3")
