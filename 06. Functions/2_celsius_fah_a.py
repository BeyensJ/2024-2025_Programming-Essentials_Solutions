# FUNCTIONS
def convert(degrees_celsius):
    return degrees_celsius * 9/5 + 32

# ASSERTS
assert celsius_fahrenheit(38) == 100.4
assert celsius_fahrenheit(39) == 102.2
assert celsius_fahrenheit(39.3) == 102.74
assert celsius_fahrenheit(40.7) == 105.26

# MAIN PROGRAM
degrees_celsius = input('Degrees Celsius: ')
while degrees_celsius != '0':
    result = str(convert(float(degrees_celsius)))
    print(degrees_celsius, 'degrees Celsius =', result, 'degrees Fahrenheit')
    print()
    degrees_celsius = input('Degrees Celsius: ')