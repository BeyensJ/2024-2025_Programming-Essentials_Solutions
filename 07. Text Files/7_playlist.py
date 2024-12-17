with open('playlist.txt', encoding='UTF-8') as file:
    lines = file.readlines()
    lines.sort()

    print('Playlist')
    for line in lines:
        if line != 'n':
            record = line.split(';')
            print(record[0], '\t', record[1].upper(), '(' + record[2].lower().rstrip() + ')')
