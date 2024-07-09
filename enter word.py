word = input("Enter the word: ")
normal_order = "".join(sorted(word))
reverse_order = normal_order[::-1]
print(f"Normal order: {normal_order}")
print(f"Reverse order: {reverse_order}")
