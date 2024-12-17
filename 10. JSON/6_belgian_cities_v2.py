import yaml

# using readline to read the file line by line

my_dict = {}
city_list = []
with open('6_belgian_cities.txt') as file:
    file.readline()  # clear title line
    line = file.readline().rstrip() # priming read!
    record = line.split(';')
    while line:
        name = record[0]
        population = record[1]
        off_lang = record[2]
        landmarks = record[3].split(',')
        is_capital_file = record[4]
        if is_capital_file == 'Y':
            is_capital = True
        else:
            is_capital = False
        city = {'name': name, 'population': int(population),
                'official_language': off_lang,
                'landmarks': landmarks, 'is_capital': is_capital}
        city_list.append(city)
        line = file.readline().rstrip()
        record = line.split(';')

my_dict['belgian_cities'] = city_list
# print(my_dict)

with open('belgian_cities2.yaml', 'w') as file:
    yaml.dump(my_dict, file, sort_keys=False)
    # sort_keys=False to preserve the order of the dictonary
