numbers = [1, -2, 3, -4, 5, -6]
negative_count = sum(1 for num in numbers if num < 0)
print(f"Negative numbers: {negative_count}")
