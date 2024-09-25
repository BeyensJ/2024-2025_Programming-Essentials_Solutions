amount_of_wine = int(input("How many bottles of wine are there: "))
amount_of_pizza = int(input("How many pizzas are there: "))

if amount_of_wine < 5 or amount_of_pizza < 5:
    print("This is just a stupid party")
else:
    if amount_of_pizza * 2 <= amount_of_wine or amount_of_wine * 2 <= amount_of_pizza:
        print("This is a fantastic party")
    else:
        print("This is a good party")
