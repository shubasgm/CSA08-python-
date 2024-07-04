def count_vowels_and_consonants(input_string):
    # Define vowels (considering both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Initialize counters
    num_vowels = 0
    num_consonants = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

# Sample input
input_statement = "Hello World"

# Count vowels and consonants
vowels_count, consonants_count = count_vowels_and_consonants(input_statement)

# Print the results
print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")

