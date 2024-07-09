def is_tech_number(n):
    temp = n
    sum_of_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    return sum_of_cubes == n

num = int(input("Enter a number: "))

if is_tech_number(num):
    print(f"{num} is a Tech number.")
else:
    print(f"{num} is not a Tech number.")
