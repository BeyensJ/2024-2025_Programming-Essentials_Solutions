boys = []
girls = []
with open('contacts.csv') as file:
    line = file.readline()
    while line:
        record = line.split(';')

        if record[3].rstrip() == 'M':
            boys.append(record[1] + ' ' + record[0])
        else:
            girls.append(record[1] + ' ' + record[0])
        line = file.readline()

boys.sort()
girls.sort()

print(len(girls), 'girls:')
for girl in girls:
    print('\t', girl)

print(len(boys), 'boys:')
for boy in boys:
    print('\t', boy)
