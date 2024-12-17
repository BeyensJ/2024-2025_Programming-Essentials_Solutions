import json

with open("3_courses.json") as json_file:
    # read out the file and parse the JSON object using the load() function:
    courses = json.load(json_file)

# for course in courses["courses"]:
#     print(course["name"])

#     for group in course["groups"]:
#         print("\t" + group["name"], end="")

#     print("\n") # new line after all groups

for course in courses["courses"]:
    print(course["name"])
    total = 0
    for group in course["groups"]:
        print("\t" + group["name"], end="")
        total += group["students"]
    print(f"\n\tTotal students for {course['name']}: {total}")
    print("") # new line after all groups

