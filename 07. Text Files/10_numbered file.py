input_file = open('7_playlist.py')
output_file = open('output_example.txt', 'w')

lines = input_file.readlines()
line_number = 1
for line in lines:
    output_file.write('{:4}'.format(line_number) + ' ' + line)
    line_number += 1

output_file.close()
input_file.close()
