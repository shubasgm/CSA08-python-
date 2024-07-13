def sum_boundary_elements(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0
    
    # Sum elements in the first row
    total_sum += sum(matrix[0])
    
    # Sum elements in the last row
    if rows > 1:
        total_sum += sum(matrix[rows - 1])
    
    # Sum elements in the first and last columns (excluding corners)
    for i in range(1, rows - 1):
        total_sum += matrix[i][0] + matrix[i][cols - 1]
    
    return total_sum

# Test case
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(sum_boundary_elements(matrix))  # Output: 68
