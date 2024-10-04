name = input('Enter your name: ')
national_number_part1 = int(input('Enter the first 9 digits of your national number : '))
national_number_part2 = int(input('Enter the last 2 digits of your national number : '))

rest = 97 - national_number_part1 % 97
if national_number_part2 != rest:
    print('Hello ' + name + ', the national number you gave is not correct')
else:
    date = national_number_part1 // 1000
    day = date % 100
    year = date // 10000
    month = date % 10000 // 100
    number = national_number_part1 % 1000
    if number % 2 == 0:
        sex = 'female'
    else:
        sex = 'male'
    print('Hi ' + name + ', you are registered as ' + sex)
    print('You were born on ' + str(day) + '/' + str(month) + '/' + str(year))

    #extend to print text month
    match month:
        case 1:
            month = "Januari"
        case 2:
            month = "Februari"
        case 3:
            month = "March"
        case 4:
            month = "April"
        case 5:
            month = "May"
        case 6:
            month = "June"
        case 7:
            month = "Juli"
        case 8:
            month = "August"
        case 9:
            month = "September"
        case 10:
            month = "October"
        case 11:
            month = "November"
        case 12:
            month = "December"
        case _:
            month = "unknown"

    print('You were born on ' + str(day) + '/' + str(month) + '/' + str(year))
