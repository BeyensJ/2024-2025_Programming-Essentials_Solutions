# This exercises is much nicer when you use lists.
# Addition: if you use lists correctly, you can play the game with any number of piles!

from random import randint

# piles = [randint(20,41), randint(20,41), randint(20,41)]
piles = [randint(20,41), randint(20,41)]

while min(piles) > 0:
    # Log-print
    # print(piles)
    
    # User's turn
    matches = int(input("How many matches do you want to take? (3-8) "))
    pile = int(input(f"Which pile do you want to take matches from? (1-{len(piles)}) "))
    
    piles[pile-1] -= matches
    
    if min(piles) <= 0:
        print("You win!")
    else:
        print(piles)

        # Computer's turn        
        piles[randint(0,1)] -= randint(3,9)
            
        if min(piles) <= 0:
            print("I win!")
    