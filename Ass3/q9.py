def is_magic_word(word):
    n = len(word)

    # Check if all letters are lowercase English alphabets
    if not all(char.islower() for char in word):
        return False

    # Check conditions for each position i
    for i in range(n // 2):
        if i % 2 == 0 and word[i] >= word[n - 1 - i]:
            return False
        elif i % 2 == 1 and word[i] <= word[n - 1 - i]:
            return False

    return True

# Get user input for the word
user_word = input("Enter a word: ")

# Check if the word is a magic word
if is_magic_word(user_word):
    print(f'The word "{user_word}" is a magic word.')
else:
    print(f'The word "{user_word}" is not a magic word.')
