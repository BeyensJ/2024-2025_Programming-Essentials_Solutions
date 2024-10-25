age = int(input('Your age: '))

if age < 6:
    print("You're too young!")
elif age <=7:
    section = "beavers"
elif age <= 10:
    section = "cubs"
elif age <= 13:
    section = "scouts"
elif age <= 18:
    section = "explorers"
else:
    section = "leaders"

print("You'll be assigned to the", section)