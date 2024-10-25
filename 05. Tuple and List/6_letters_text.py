letters = []
text = input('Enter a text: ')
for i in range(len(text)):
    if text[i] != ' ': # and not text[i] in letters:
        letters.append(text[i])

# letters.sort()
print(letters)
print()
print(*letters)
print()
for item in letters:
    print(item, '\t', end='')
