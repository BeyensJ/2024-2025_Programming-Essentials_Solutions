with open('first_names.txt') as file:
    first_names = file.readlines()
    counter = 0
    while counter < len(first_names):
        print(first_names[counter].rstrip().ljust(13), end='')
        counter += 1
        if counter % 10 == 0:
            print()
