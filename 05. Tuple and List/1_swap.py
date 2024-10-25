animal_names = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print('Original list:', '\t\t', animal_names)
help = animal_names[0]
animal_names[0] = animal_names[len(animal_names) - 1]
animal_names[len(animal_names) - 1] = help
print('After the switch:','\t', animal_names)

# or:
# animal_names = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']
# print('Original list: ', animal_names)
# animal_names[0], animal_names[-1] = animal_names[-1], animal_names[0]
# print('After switching: ', animal_names)

# or:
# animal_names = animal_names[-1:] + animal_names[1:-1] + animal_names[:1]
