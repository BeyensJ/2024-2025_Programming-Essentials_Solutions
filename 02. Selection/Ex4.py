first_number = int(input("Number 1: "))
second_number = int(input("Number 2: "))
third_number = int(input("Number 3: "))

if (first_number == second_number + third_number or
        second_number == first_number + third_number or
        third_number == second_number + first_number):
    print("This works")
else:
    print("This won't work")
