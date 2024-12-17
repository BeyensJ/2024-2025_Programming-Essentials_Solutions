import json

filename = '1_fictional_rodents.json'

with open(filename) as file:
    rodents = json.load(file)

# printing the rodents
for rodent in rodents:
    print(rodent)
    for item in rodents[rodent]:
        # print(f"\t{item}")
        print(f"\t{item['character']}: {item['notes']}")

new_squirrel = {
    "character": "Felldoh",
    "author": "Brian Jacques",
    "work": "Martin the Warrior",
    "notes": "A young red squirrel."
}

# rodents["squirrels"].append(new_squirrel)

with open(filename, 'w') as outfile:
    json.dump(rodents, outfile, indent=3)
