choice_computer = "paper"
choice_player = input("What do you choose: paper, rock or scissors? ")
if choice_computer == choice_player:
    answer = "Tie!"
else:
    if choice_computer == "paper":
        if choice_player == "rock":
            answer = "I win :-)"
        else:
            answer = "You win :-)"
    else:
        if choice_computer == "rock":
            if choice_player == "scissors":
                answer = "I win :-)"
            else:
                answer = "You win :-)"
        else:  # Computer choice must be scissors
            if choice_player == "paper":
                answer = "I win :-)"
            else:
                answer = "You win :-)"

print('You chose', choice_player)
print('I chose', choice_computer)
print(answer)
