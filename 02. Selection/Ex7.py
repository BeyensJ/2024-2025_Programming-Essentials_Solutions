number1 = int(input('First number: '))
number2 = int(input('Second number: '))
if number1 == number2:
    output = 0
else:
    if number1 % 5 == number2 % 5 == 0:
        # or    if number1 % 5 == 0 and number2 %5 == 0
        if number1 < number2:
            output = number1
        else:
            output = number2
    else:
        if number1 > number2:
            output = number1
        else:
            output = number2
print('The answer for the numbers', number1, 'and', number2, '=', output)
