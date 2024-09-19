# INPUT:
surname = input('surname: ') # space behind ":", otherwise the answer is pasted to the question
first_name = input('first name: ')
street = input('street: ')
number = input('number: ')
zip_code = input('zip code: ')
city = input('city: ')

# Note:
# surname = str(input('surname: ')) # is wrong. It works, but the "str" function does nothing as the input-function already returns a string.
# number = int(input('number: ')) # is strictly correct, but we don't need to convert the input to an integer, as we can just print it as a string. It will also make printing more difficult, as we will have to convert it back to a string.

# PRINTING:
# First method:
print(first_name + ' ' + surname) # Note the added space
print(street,number) # Note how we didn't (need to) ad a space
print(zip_code, city)

# Second method:
# This method is wrong! You get the information on three lines, but the second and third line start with a space
print(first_name, surname, '\n', street, number, '\n', zip_code, city)

# Third method:
# This is an adapted version of the second method, which is correct but much more complicated
print(first_name, surname, '\n' + street, number, '\n' + zip_code, city)

# Fourth method:
# We're printing three lines without any spaces in front. This is a very clean way of printing the information, much less complicated than the second way.
print(first_name + " " + surname + "\n" + street + " " + number + "\n" + zip_code + " " + city)

