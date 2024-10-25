my_age = int(input("How old are you? "))
fathers_age = int(input("How old is your father? "))

if fathers_age / my_age < 2:
# if fathers_age / 2 < my_age:
# if fathers_age < my_age * 2:
    print("The situation is no longer possible for your ages")
else:
    i = 0
    while fathers_age / my_age > 2:
        i += 1
        fathers_age += 1
        my_age += 1
    print("Within", i, "years, your father will have twice your age")
    print("Your father will be", fathers_age, "and you will be", my_age)