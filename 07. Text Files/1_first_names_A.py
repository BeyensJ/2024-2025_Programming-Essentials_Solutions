with open('first_names.txt') as file:
    name = file.readline()
    number = 0
    total_number = 0
    while name:
        total_number += 1
        if 'z' in name or 'Z' in name:    
            print(name.rstrip())
            number += 1
        name = file.readline()

    
print(f"There are {total_number} first names in the file.")
print(f"{number} of which contain a letter z.")