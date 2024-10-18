word = input('Enter a word: ')
reverse = word[::-1]

if reverse == word:
    print(word, 'is a palindrome.')
else:
    print(word, 'is not a palindrome.')