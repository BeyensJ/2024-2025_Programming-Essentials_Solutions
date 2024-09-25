first_number = int(input("First number: "))
second_number = int(input("Second number: "))
biggest_number = 0;

if first_number < 0:
    first_number *= -1

if second_number < 0:
    second_number *= -1

if first_number > second_number:
    biggest_number = first_number

if second_number > first_number:
    biggest_number = second_number

print("The answer for the numbers", first_number, "and", second_number, "=", biggest_number)
