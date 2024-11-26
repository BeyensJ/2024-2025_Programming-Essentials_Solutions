#IMPORTS
import random

#FUNCTIONS
def roll_dice(number_of_dices):
    result = []
    throw = 0
    while throw < number_of_dices:
        result.append(random.randint(1,6))
        throw += 1
    return result

#ASSERTS
#NO ASSERTS POSSIBLE

#MAIN PROGRAM
counter = 0
poker = False
dices = int(input('How many dices you want to work with: '))

while not poker:
    to_check = roll_dice(dices)
    counter += 1
    poker = True

    for i in range(len(to_check)-1):
        if to_check[i] != to_check[i+1]:
            poker = False


print(to_check)
print('After ' + str(counter) + ' rolles we got a poker!')



