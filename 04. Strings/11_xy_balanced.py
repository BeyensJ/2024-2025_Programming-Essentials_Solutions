text = input('Enter a text: ')
i = 0
gevolgd = True

while gevolgd and i < len(text):
    if text[i] == 'x':
        if text[i:].find('y') == -1:
            gevolgd = False
    i += 1

if gevolgd:
    print('In this text every x is followed by a y.')
else:
    print('In this text not every x is followed by a y.')

# alternative:
string = input("Enter a text: ")
position_x = string.rindex("x")
position_y = string.rindex("y")

if position_x < position_y:
    print("In this text, every x is followed by a y")
else:
    print("In this text, not every x is followed by a y")