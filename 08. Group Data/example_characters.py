text = input('Enter a (grouped) sequence of characters: ')
print('The compressed text: ', end='')
i = 0

while i < len(text):
    characterind = text[i]
    number_characters = 0
    while i < len(text) and text[i] == characterind:
        number_characters += 1
        i += 1
    print('('+str(number_characters)+characterind+')', end='')

print()