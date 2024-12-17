with open('classrooms.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')        # Naam;Voornaam;lokaal
    while line:
        number_per_room = 0
        roomind = record[2]
        print(roomind)
        while line and record[2] == roomind:
            number_per_room += 1
            print("\t", record[1], record[0])
            line = file.readline().rstrip()
            record = line.split(';')
        print('Number of students in classroom', roomind, '=', number_per_room)
