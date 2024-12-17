with open('books.txt') as file:
    line = file.readline()
    counter = 1
    while line:
        author = file.readline()
        print(str(counter) + ".", line.rstrip(), '->', author.rstrip())
        line = file.readline()
        counter += 1