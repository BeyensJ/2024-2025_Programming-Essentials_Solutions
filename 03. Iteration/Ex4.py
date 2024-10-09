number_to_guess = 15
turns = 0
guess = -1

while guess != number_to_guess:
   guess = int(input("Enter a positive number: "))
   turns += 1
   if guess < number_to_guess:
       print("Higher!")
   if guess > number_to_guess:
       print("Lower!")

print("You have guessed the number", number_to_guess, "in", turns, "turns")
