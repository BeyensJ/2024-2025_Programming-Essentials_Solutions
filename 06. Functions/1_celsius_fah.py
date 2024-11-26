

def convert(_celsius):
    _Fahrenheit = _celsius * 9/5 + 32
    print(_celsius, "celsius = ", _Fahrenheit, 'degrees Fahrenheit')
    return _Fahrenheit

#MAIN
degrees_celsius = float(input('Degrees Celsius: '))
degrees_Fahrenheit = convert(degrees_celsius)
print(str(degrees_celsius), 'degrees Celsius =', str(degrees_Fahrenheit), 'degrees Fahrenheit')
