input_string = input("Enter a text consiting only of letters and number: ")
numbers = set()
letters = set()
for character in input_string:
    if character.isdigit():
        numbers.add(character)
    else:
        letters.add(character)
        
        
print('The numbers:')
for digit in numbers:
    print(digit)
print('The Letters:')
for letter in letters:
    print(letter)
