number = int(input("Enter a number: "))
zeros = 0
sixes = 0

while number != 0:
    digit = number % 10
    if digit == 0:
        zeros += 1
    if digit == 6:
        sixes += 1
    number //= 10

print("The number consists of", zeros, "zeros and", sixes, "sixes")