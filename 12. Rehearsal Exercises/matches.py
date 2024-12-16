import json
import yaml

#program start instructions
with open('matches.txt') as file:
    lines = file.readlines()

rounds = []
i = 0
record = lines[i].split(';')

#while not_end_data
while i < len(lines):

    # group start instructions:
    matchdayind = record[0]
    matches = []

    #while not_end_data and in_the_same_group
    while i < len(lines) and record[0] == matchdayind:

        #actions for that one element of the group
        match = dict()
        match["date"] = record[1]
        match["home"] = record[2]
        match["visitors"] = record[3]

        score = dict()
        score["final"] = record[4].rstrip()

        match["score"] = score

        matches.append(match)

        #take next element of the group
        i+= 1
        if i < len(lines):
            record = lines[i].split(';')

    #group final instructions:
    round = dict()
    round["name"] = matchdayind
    round["matches"] = matches
    rounds.append(round)

#program final instructions
result = dict()
result["results"] = rounds

with open('matches.json', 'w', encoding="UTF-8") as file:
    json.dump(result, file, indent=3)

with open('matches.yaml', 'w', encoding="UTF-8") as file:
    yaml.dump(result, file, indent=3)


