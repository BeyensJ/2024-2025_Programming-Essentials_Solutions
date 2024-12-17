input_file = open('output_example.txt')
output_file = open('nonumber.py', 'w')

lines = input_file.readlines()
for line in lines:
    output_file.write(line[5:])

output_file.close()
input_file.close()
