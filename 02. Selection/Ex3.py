smallest_number = int(input("Number 1: "))

number = int(input("Number 2: "))
if number < smallest_number:
    smallest_number = number

number = int(input("Number 3: "))
if number < smallest_number:
    smallest_number = number

print("The smallest number is", smallest_number)
