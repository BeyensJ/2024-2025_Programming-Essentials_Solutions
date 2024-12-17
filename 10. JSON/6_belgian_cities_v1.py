import yaml

# using readlines to read the file in one big go

with open('6_belgian_cities.txt') as file:
    lines = file.readlines()

lines.pop(0)
my_dict = {}
cities = []

for line in lines:
    record = line.split(';')
    name = record[0]
    population = record[1]
    off_lang = record[2]
    landmarks = record[3].split(',')
    is_capital_file = record[4].rstrip()
    if is_capital_file == 'Y':
        is_capital = True
    else:
        is_capital = False
    city = {'name': name, 'population': int(population), 'official_language': off_lang,
            'landmarks': landmarks, 'is_capital': is_capital}
    cities.append(city)

my_dict['belgian_cities'] = cities

with open('Belgian_cities.yaml', 'w') as file:
    yaml.dump(my_dict, file, sort_keys=False)
