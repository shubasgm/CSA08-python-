# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Printing the dictionary items
print("Dictionary Items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Printing the dictionary keys
print("\nDictionary Keys:")
for key in my_dict.keys():
    print(key)

# Copying the dictionary
copied_dict = my_dict.copy()
print("\nCopied Dictionary:")
print(copied_dict)
