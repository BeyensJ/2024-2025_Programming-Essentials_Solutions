python_classes=[['1ITFA', 35]]
total = python_classes[0][1]
for i in range(ord('B'), ord('B')+7):
     number = int(input ('Number of students in 1ITF' + chr(i) + ': '))
     python_classes.append(['1ITF'+chr(i), number])
     total += number
print(*python_classes, sep="\n")
print(total, 'students follow the Python course.')

