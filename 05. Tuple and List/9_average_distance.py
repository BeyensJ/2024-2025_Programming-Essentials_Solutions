names = []
distances = []
print('Enter your name and the distance to school.')
print('Type stop when you want to close the entry.')
name = input('Your name: ')
#read all names and distances and immediately calculate largest and sum
while name != 'stop':
    distance = float(input('Distance to school: '))
    names.append(name)
    distances.append(distance)
    name = input('Your name: ')

#print lists and conclusions
if len(names) != 0:
    print('Overview')
    for i in range(len(names)):
        print(names[i], '\t', distances[i])
    max = max(distances)
    print(names[distances.index(max)], 'lives farthest, namely', max, 'km')
    print('The average distance is', sum(distances)/len(distances))

