#IMPORTS
import random

#FUNCTIONS
def password_structure(structure_length):
    password_check = False

    while not password_check:
        password_structure = []

        i = 0
        while i < structure_length:
            password_structure.append(random.randint(1,4))
            i+=1

        if 1 in password_structure and 2 in password_structure and 3 in password_structure and 4 in password_structure:
            password_check = True

    return password_structure

def password_creator(length):
    if length < 4:
       length = 4

    password_list = password_structure(length)
    password = ""

    i = 0
    while i < len(password_list):
        match password_list[i]:
            case 1:
                #lower case character
                random_lower_letter = chr(random.randint(ord('a'), ord('z')))
                password += random_lower_letter
            case 2:
                #upper case character
                #randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
                #or ...
                list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                random_upper_letter = list_upper[random.randint(0, len(list_upper)-1)]
                password += random_upper_letter
            case 3:
                #digit
                random_digit = random.randint(0, 9)
                password += str(random_digit)
            case 4:
                #punctuation mark
                marks = ['#', '!', '$', '%', '&']
                random_mark = marks[random.randint(1, 4)]
                password += random_mark
        i+=1

    return password

#ASSERTS
#NO ASSERTS POSSIBLE

#MAIN PROGRAM
how_many = int(input('How many password do you want to generate? '))
while how_many < 1:
    how_many = int(input('How many password do you want to generate? (should be possitive number) '))

length_pwd = int(input('What should the password length? '))
if length_pwd < 4:
    print('Password that will be generated, will have minimum length of 4')
    length_pwd = 4

for x in range(how_many):
    print(password_creator(length_pwd))
