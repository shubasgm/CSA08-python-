def count_vowels_and_consonants(statement):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0
    
    for char in statement:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    print(f"Number of vowels = {vowel_count}")
    print(f"Number of consonants = {consonant_count}")
    
    if vowel_count > consonant_count:
        print("Vowels are more.")
    elif consonant_count > vowel_count:
        print("Consonants are more.")
    else:
        print("Both are equal.")

# Sample Input
statement = "Saveetha School of Engineering"

# Function Call
count_vowels_and_consonants(statement)
