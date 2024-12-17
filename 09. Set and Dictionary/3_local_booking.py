with open('local_booking_2023.txt') as file:
    classrooms_set = set()
    line = file.readline().rstrip()
    while line:
        record = line.split(';')
        classroom = record[3]
        classrooms_set.add(classroom)
        line = file.readline().rstrip()
print('Classrooms:')
for classroom in sorted(classrooms_set):
    print(classroom)
