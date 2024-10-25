sentence = ""
for i in range(1, 6):
    word = input('Enter word ' + str(i) + ': ')
    word = word.capitalize()
    sentence = word + ' ' + sentence

print('The words in reverse order: ')
print(sentence)