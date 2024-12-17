import random

number = random.randint(1, 10)
name = 'wish'+str(number)+'.txt'

print('Wish', number, '\n')
with open(name) as file:
    print(file.read())
