animal_names = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print('Original list:\t', animal_names)
start = animal_names[0]
animal_names.remove(animal_names[0])
animal_names.append(start)
print('After sliding:\t', animal_names)

# of
animal_names = animal_names[1:] + animal_names[:1]
print('After sliding:\t', animal_names)
