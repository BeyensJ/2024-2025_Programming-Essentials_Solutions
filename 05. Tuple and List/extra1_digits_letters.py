digits = []
letters = []

text = input('Pass your string of characters: ')
for character in text:
     if character.isdigit():
         digits.append(character)
     elif character.islower():
         letters.insert(0, character)
     elif character.isupper():
         letters.append(character)
newlist = digits + letters
print(newlist)
