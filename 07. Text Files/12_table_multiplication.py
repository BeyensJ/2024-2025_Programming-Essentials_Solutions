import random

number = random.randint(1, 10)
name_file = 'table_' + str(number) + '.txt'
output_file = open(name_file, 'w')

for counter in range(1, 11):
    output_file.write(str(counter) + 'x' + str(number) + '=' + str(counter * number) + '\n')

output_file.close()
