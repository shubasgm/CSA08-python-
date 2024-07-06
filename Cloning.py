a = [1, 2, 3, 4, 5]

b = a

print("Original list a:", a)
print("Alias list b:", b)

a.append(6)
a[1] = 10

print("\nAfter modifying list a:")
print("Modified list a:", a)
print("Alias list b:", b)

if a is b:
    print("\nChanges made in list 'a' are reflected in list 'b' because they are the same object.")
else:
    print("\nLists 'a' and 'b' are different objects.")
