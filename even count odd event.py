numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
