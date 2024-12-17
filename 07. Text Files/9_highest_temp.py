with open("weather_2018 08.csv") as file:
    # read first line with field names
    line = file.readline()

    list_temperatures = []
    line = file.readline()
    while line:
        date_info = line.split(';')
        list_temperatures.append(date_info[1])
        line = file.readline()

print('The highest temperature in this period =', max(list_temperatures), '°C')
