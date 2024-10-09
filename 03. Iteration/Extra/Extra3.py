from random import randint

pile_1 = randint(20,41)
pile_2 = randint(20,41)

while pile_1 > 0 and pile_2 > 0:
    # Log-print
    # print(pile_1, pile_2)
    # Better: https://realpython.com/python-logging/
    
    # User's turn
    matches = int(input("How many matches do you want to take? (3-8) "))
    pile = int(input("Which pile do you want to take matches from? (1/2) "))
    
    if pile == 1:
        pile_1 -= matches
    else:
        pile_2 -= matches
    
    if pile_1 < 0 or pile_2 < 0:
        print("You win!")
    else:
        print(pile_1, pile_2)
        
        # Computer's turn
        if randint(1,2) == 1:
            pile_1 -= randint(3,9)
        else:
            pile_2 -= randint(3,9)
            
        if pile_1 < 0 or pile_2 < 0:
            print("I win!")
    