def count_special_characters(input_string):
    special_characters = 0
    
    # Define special characters
    special_chars = set("!@#$%^&*()_+-=[]{};:'\"\\|<>,./?")
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a special character
        if char in special_chars:
            special_characters += 1
    
    return special_characters

# Sample input
input_statement = "#&$% is the wishes"

# Count special characters
num_special_chars = count_special_characters(input_statement)

# Print the result
print(f"Special Characters: {num_special_chars}")

