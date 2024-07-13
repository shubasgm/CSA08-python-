def add_binary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    
    # Pad the shorter string with leading zeros
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Initialize the result and carry
    result = []
    carry = 0
    
    # Perform binary addition from right to left
    for i in range(max_len - 1, -1, -1):
        bit_sum = carry
        bit_sum += 1 if a[i] == '1' else 0
        bit_sum += 1 if b[i] == '1' else 0
        
        # Determine the resulting bit and the carry
        result.append('1' if bit_sum % 2 == 1 else '0')
        carry = 0 if bit_sum < 2 else 1
    
    # If there's a carry left, append it
    if carry != 0:
        result.append('1')
    
    # The result list is in reverse order, reverse it to get the final result
    result.reverse()
    
    return ''.join(result)

# Test case
a = "11"
b = "1"
print(add_binary(a, b))  # Output: "100"
