color = input('What is your favourite color: ')

print(color[0]+color[2])
print("This color consists of " + str(len(color)) + " letters")
print()

for letter in color:
    print(letter + ' = ' + str(ord(letter)))
print()

i= 0
while i < len(color):
    if i % 2 == 0:
        print('#' + color[i]+'#')
    else:
        print('**' + color[i]+'**')
    i += 1