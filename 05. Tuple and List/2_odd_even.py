numbers = [23, 12, 54, 85, 46, 30, 26, 64, 91]

new_list = []
for number in numbers:
    if number % 2 == 0:
        new_list.insert(0,number)
    else:
        new_list.append(number)
print(numbers, 'becomes', new_list)
