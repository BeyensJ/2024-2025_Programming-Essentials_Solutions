#import random
from random import randint
def generate_list(number, lower, upper):
     random_list=[]
     for i in range(number):
         random_list.append(randint(lower,upper))
     return random_list

def filter_list(list):
    list_unique_values=[]
    for item in list:
        if not item in list_unique_values:
            list_unique_values.append(item)
    #print("unique list =", list_unique_values)
    return(list_unique_values)

# # program 1
# number_of_dice= int(input('How many dice do you want to roll? '))
# list_random_values = generate_list(number_of_dice,1,6)
# print('You threw: ', list_random_values)
# print('Your unique rolls were: ', filter_list(list_random_values))
#
# Program 2: Poker
list_random_values = generate_list(5,1,6)
counter = 0
while len(filter_list(list_random_values)) != 1:
     #print('You threw: ', list_random_values)
     counter +=1
     list_random_values = generate_list(5, 1, 6)
print('You threw: ',list_random_values)
print('You threw poker after', counter, 'times.')