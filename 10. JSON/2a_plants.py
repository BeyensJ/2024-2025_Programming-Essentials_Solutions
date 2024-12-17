
import json

with open("ex1_plants.json") as json_file:
    # read out the file and parse the JSON object using the load() function:

    plants = json.load(json_file)

print(plants)

