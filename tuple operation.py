# Creating tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)

# Tuple Concatenation
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Tuple Repetition
repeated_tuple = tuple1 * 2
print("Repeated Tuple:", repeated_tuple)

# Accessing Elements
first_element = tuple1[0]
print("First Element of tuple1:", first_element)

# Slicing a Tuple
sliced_tuple = tuple1[1:4]
print("Sliced Tuple (1:4):", sliced_tuple)

# Tuple Length
tuple_length = len(tuple1)
print("Length of tuple1:", tuple_length)

# Tuple Methods
# Count method
count_of_2 = tuple1.count(2)
print("Count of 2 in tuple1:", count_of_2)

# Index method
index_of_3 = tuple1.index(3)
print("Index of 3 in tuple1:", index_of_3)

# Membership Test
is_4_in_tuple1 = 4 in tuple1
print("Is 4 in tuple1:", is_4_in_tuple1)

# Iterating through a Tuple
print("Elements in tuple1:")
for element in tuple1:
    print(element)

# Unpacking Tuples
a, b, c, d, e = tuple1
print("Unpacked Elements:", a, b, c, d, e)
