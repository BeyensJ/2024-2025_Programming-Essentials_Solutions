room_list = []
with open('classrooms.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        roomind = record[2]
        number_per_room = 0

        while line and record[2] == roomind:
            # print('\t' + record[1]+ ' ' + record[0])
            number_per_room += 1
            line = file.readline().rstrip()
            record = line.split(';')

        room_list.append([roomind, number_per_room])

print(*room_list)
