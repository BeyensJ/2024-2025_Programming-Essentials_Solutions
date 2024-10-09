product = 1

number = int(input("Enter a number: "))
if number == 0:
    print("no numbers entered")
else:

    largest = number
    smallest = number
    
    while number != 0:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        number = int(input("Enter a number: "))
    print("The difference between the largest number", largest, "and the smallest", smallest,"=", largest-smallest)