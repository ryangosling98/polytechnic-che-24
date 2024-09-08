word = input("Enter a word: ")

# Remove spaces and convert to lowercase
word = word.replace(" ", "").lower()

# Check if the word is equal to its reverse
reversed_word = word[::-1]
if word == reversed_word:
    print(word, "is a palindrome!")
else:
    print(word, "is not a palindrome.")