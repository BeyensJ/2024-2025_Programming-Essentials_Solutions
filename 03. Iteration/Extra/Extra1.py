limit = int(input("Up to which limit would you like to print the sequence of Fibonnacci? "))

number = 1
number_minus1 = 0
if limit == 0:
    print("0")
else:
    print("0, 1", end="")
    while number + number_minus1 < limit:
        temp = number_minus1
        number_minus1 = number
        number = temp + number_minus1
        print(",", number, end="")

