with open('courses.csv') as input_file:
    with open('students.csv', 'w') as output_file:

        input_file.readline()                   # read title line and do nothing with it
        line = input_file.readline().rstrip()   # read first real info
        record = line.split(';')
        while line:
            studentind = record[3]
            student_info = studentind+';' + record[4] + ';' + record[5]
            while line and record[3] == studentind:
                student_info += ';'+record[1]+' ('+record[2] + ')'
                line = input_file.readline().rstrip()   # read next line
                record = line.split(';')
            output_file.write(student_info + '\n')
            print(student_info)     # ter controle
