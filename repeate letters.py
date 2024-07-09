def find_repeated_letters():
    word = input("Enter a word: ")
    word = word.lower()  # convert to lowercase to ignore case sensitivity
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    repeated_letters = [letter for letter, count in letter_count.items() if count > 1]

    print("Repeated letters:")
    for letter in repeated_letters:
        print(letter)

    print(f"Number of repeated letters: {len(repeated_letters)}")

find_repeated_letters()
