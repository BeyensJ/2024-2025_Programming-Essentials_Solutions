import json

all_orders = list()

name = input('Name of the club member: ')  # priming read
order_person = dict()

while name.lower() != 'end':
    short = input('Short size: ')
    tshirt = input('T-shirt size: ')
    backp = input('New Backpack? (Y/N) ').lower()
    if backp.lower() == 'y':
        backpack = True
    else:
        backpack = False

    order_short = {'short': short}
    order_tshirt = {'t-shirt': tshirt}
    order_backpack = {'backpack': backpack}

    order_list = [order_short, order_tshirt, order_backpack]
    order_person[name] = order_list
    all_orders.append(order_person)

    print()
    name = input('Name of the club member: ')  # modifying read
    order_person = dict()

new_order = {'club_order': all_orders}

with open("club_order.json", "w", encoding="UTF-8") as file:
    json.dump(new_order, file, indent=3)
