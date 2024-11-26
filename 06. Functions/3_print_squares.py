def print_square(_sign, _number):
    """
    This function constructs a string with a number amount of symbols
    :param _sign: The symbol that it printed
    :param _number: number of occurrences of the symbol
    :return: string containing the symbol a number of times
    """
    line = _number * _sign
    return line

#MAIN
sign = input('Which character must be used to form the lines (enter = stop): ')
while sign != '':
    number = int(input('Number of characters per line = number of lines = '))
    for i in range(number):
        print(print_square(sign, number))
    sign = input('Which character must be used to form the lines (enter = stop): ')

print("call the print")