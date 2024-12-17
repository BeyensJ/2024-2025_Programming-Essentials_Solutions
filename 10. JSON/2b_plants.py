import json

with open("ex1_plants.json") as json_file:
    # read out the file and parse the JSON object using the load() function:
    plant_dict = json.load(json_file)
    plant_list = plant_dict["catalog"]

teller = 1
for plant in plant_list:
    print("Plant number " + str(teller))
    for key_value in plant:
        print('\t', key_value, plant[key_value])
    teller += 1
