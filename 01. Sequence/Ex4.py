first_name = input("Enter the first name: ")
second_name = input("Enter the second name: ")

print("Before changing: " + first_name + " " + second_name)

intermediate = second_name
second_name = first_name
first_name = intermediate

print("After changing: " + first_name + " " + second_name)

# Also works, but not in all languages:
# first_name, second_name = second_name, first_name
# Good for you if you found it, but don't worry if you didn't.