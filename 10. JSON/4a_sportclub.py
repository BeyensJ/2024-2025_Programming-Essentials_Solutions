import json

all_orders = dict()

name = input('Name of the club member: ')
while name.lower() != 'end':
    short = input('Short size: ').upper()

    if short == 'XS':
        if "short extra small" in all_orders:
            all_orders["short extra small"] += 1
        else:
            all_orders["short extra small"] = 1
    elif short == 'S':
        if "short small" in all_orders:
            all_orders["short small"] += 1
        else:
            all_orders["short small"] = 1
    elif short == 'M':
            if "short medium" in all_orders:
                all_orders["short medium"] += 1
            else:
                all_orders["short medium"] = 1
    elif short == 'L':
            if "short large" in all_orders:
                all_orders["short large"] += 1
            else:
                all_orders["short large"] = 1
    elif short == 'XL':
            if "short extra large" in all_orders:
                all_orders["short extra large"] += 1
            else:
                all_orders["short extra large"] = 1

    tshirt = input('T-shirt size: ').upper()

    if tshirt == 'XS':
        if "t-shirt extra small" in all_orders:
            all_orders["t-shirt extra small"] += 1
        else:
            all_orders["t-shirt extra small"] = 1
    elif tshirt == 'S':
        if "t-shirt small" in all_orders:
            all_orders["t-shirt small"] += 1
        else:
             all_orders["t-shirt small"] = 1
    elif tshirt == 'M':
            if "t-shirt medium" in all_orders:
                all_orders["t-shirt medium"] += 1
            else:
                all_orders["t-shirt medium"] = 1
    elif tshirt == 'L':
            if "t-shirt large" in all_orders:
                all_orders["t-shirt large"] += 1
            else:
                all_orders["t-shirt large"] = 1
    elif tshirt == 'XL':
            if "t-shirt extra large" in all_orders:
                all_orders["t-shirt extra large"] += 1
            else:
                all_orders["t-shirt extra large"] = 1

    backpack = input('New Backpack? (Y/N) ').lower()

    if backpack == "y":
        if "backpacks" in all_orders:
            all_orders["backpacks"] += 1
        else:
            all_orders["backpacks"] = 1

    print()
    name = input('Name of the club member: ')

new_order = {"Club order": all_orders}

with open("Club_order.json", "w", encoding="UTF-8") as file:
    json.dump(new_order, file, indent=3)
