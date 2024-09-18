surname = input("Surname: ")
first_name = input("First name: ")
street = input("Street: ")
number = input("Number: ")
zip_code = input("Zip code: ")
city = input("City: ")

# With '+' operator
print(first_name + " " + surname + "\n" + street + " " + number + "\n" + zip_code + " " + city)

# Without '+' operator
print(first_name, surname)
print(street, number)
print(zip_code, city)
