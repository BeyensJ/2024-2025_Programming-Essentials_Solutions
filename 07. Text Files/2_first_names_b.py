with open('first_names.txt') as file:
    first_names = file.readlines()

# first_names.reverse()
# for name in first_names:
#     print(name, end='')

# for name in first_names[::-1]:
#     print(name, end='')

for name in reversed(first_names):
    print(name, end='')