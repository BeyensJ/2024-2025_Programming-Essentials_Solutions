with open('hamlet.txt', 'r') as input_file:
    lines = input_file.readlines()


output_file = open('hamlet2.txt', 'w')

for line in lines:
    for character in ',.;:?!':
        line = line.replace(character+'  ', character+' ')
    output_file.write(line)


output_file.close()