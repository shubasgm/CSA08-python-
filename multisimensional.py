# Creating a multidimensional list
multi_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the multidimensional list
for row in multi_list:
    for element in row:
        print(element, end=' ')
    print()
