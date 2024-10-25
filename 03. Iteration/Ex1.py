product = 1

number = int(input("Enter a number, stop by entering a zero: "))
i = 0
while number != 0:
    product *= number
    number = int(input("Enter a number, stop by entering a zero: "))
    i += 1
print("The product of the", i, "numbers is", product)