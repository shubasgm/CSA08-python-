def create_tuple_list(n):
    tuple_list = [(i, i*i) for i in range(1, n+1)]
    return tuple_list

# Example usage:
n = 10
result = create_tuple_list(n)
print(result)
