check_number = int(input("What final digit do you want to check the numbers on? "))
amount = 0

for i in range(0, 10):
    number = int(input("Enter a number: "))
    if number % 10 == check_number:
        amount += 1

print(amount, "out of 10 numbers end on", check_number)
