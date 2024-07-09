n = int(input("Enter the number of elements: "))
my_list = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
index = int(input("Enter the index: "))
element = int(input("Enter the element: "))
my_list.insert(index, element)
print(my_list)
