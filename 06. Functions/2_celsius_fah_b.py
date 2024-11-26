# FUNCTIONS
def celsius_fahrenheit(degrees_celsius):
    return degrees_celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# ASSERTS
assert celsius_fahrenheit(38) == 100.4
assert celsius_fahrenheit(39) == 102.2
assert celsius_fahrenheit(39.3) == 102.74
assert celsius_fahrenheit(40.7) == 105.26
assert fahrenheit_celsius(99.5) == 37.5
assert fahrenheit_celsius(101.3) == 38.5
assert fahrenheit_celsius(104) == 40
assert fahrenheit_celsius(107.6) == 42

# MAIN PROGRAM
answer = input('Do you want to convert starting from Celsius (enter C) or Fahrenheit (enter F): ').upper()
while answer == 'C' or answer == 'F':
    convert_from = float(input('Degrees: '))
    if answer.upper() == 'C':
        result = str(celsius_fahrenheit(convert_from))
        print(convert_from, 'degrees Celsius =', result, 'degrees Fahrenheit')
    else:
        result = str(fahrenheit_celsius(convert_from))
        print(convert_from, 'degrees Fahrenheit =', result, 'degrees Celcius')
    print()
    answer = input('Do you want to convert starting from Celsius (enter C) or Fahrenheit (enter F): ').upper()