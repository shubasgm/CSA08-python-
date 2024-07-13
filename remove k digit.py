def removeKdigits(num: str, k: int) -> str:
    stack = []
    
    for digit in num:
        # Remove digits from the stack if the current digit is smaller than the stack's top
        # This ensures that the stack remains in increasing order
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If there are still digits to remove, remove from the end
    while k > 0:
        stack.pop()
        k -= 1
    
    # Remove leading zeros and convert to string
    result = ''.join(stack).lstrip('0')
    
    return result if result else '0'

# Test case
num = "1432219"
k = 3
print(removeKdigits(num, k))  # Output: "1219"
