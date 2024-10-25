name = input('Your name (press enter to stop): ')
print()
while name != '':
    print('Menu:', len('Menu:')*'*', 'U Uppercase', 'L Lowercase', 'A Alternate', sep='\n')
    choice = ' '
    while 'ULA'.find(choice) == -1:
        choice = input('Make a choice (U-L-A): ').upper()
    if choice == 'U':
        print(name.upper())
    elif choice == 'L':
        print(name.lower())
    elif choice == 'A':
        for i in range(0, len(name)):
            if i % 2 == 0:
                print(name[i].upper(), end='')
            else:
                print(name[i].lower(), end='')

    print()
    name = input('Your name (press enter to stop): ')