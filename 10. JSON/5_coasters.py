import yaml

with open('roller_coasters.yaml', 'r', encoding='UTF-8') as file:
    roller_coasters_dict = yaml.safe_load(file)

countries = roller_coasters_dict['countries']
themeparks = []

for country in countries:
    print(country['name'])
    print('*' * len(country['name']))
    for park in country['parks']:
        for ride in park['ride_types']:
            for roller_coaster in ride['rollercoasters']:
                print('- ' + roller_coaster['name'] + ' --> ' + roller_coaster['speed'])
    print()
