import json

with open("ex1_plants.json") as json_file:
    # read out the file and parse the JSON object using the load() function:
    plants_json = json.load(json_file)
    plants = plants_json["catalog"]

teller = 1
for plant in plants:
    if plant['light'] == "SUN":
        print('Plant number', teller)
        print("\t" + "Name: " + plant['common'] + " (" + plant['botanical'].lower() + ")")
        print("\t" + "Light: " + plant['light'])
        print("\t" + "Price: " + plant['price'])
        teller += 1
