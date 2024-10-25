# films = ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji']
# films2 = ['IT', 'Once upon a time', *films[1:-1], 'Bad Cop']
# print(films2)
# dia 12
# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# day = input('Enter a day: ')
# if day in weekdays[0:5]:
#     print('Weekday')
# elif day in weekdays[5:]:
#     print('Weekend')
# else:
#     print('Input not in series:', *weekdays)

# # dia 14
# films = ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji']
# new_film = input("Which movie would you like to add? ")
#
# while not new_film in films:
#     films.append(new_film)
#     print(new_film, "has been added. \nYour collection contains", len(films), "films.")
#     new_film = input("\nWhich movie would you like to add? ")
#
# # when an existing movie is entered, we show the overview
# print("This film is already in your collection!")
# print("Overview collection")
# for film in films:
#     print(film)
#
# # dia 19
# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# for day in weekdays:
#     print(day)
# dia 20
# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# for i in range(len(weekdays)):
#     print(weekdays[i])
# dia 21
# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# index = 0
# while index < len(weekdays):
#     print(weekdays[index])
#     index += 1

# dia 22
# films = ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji']
# for film in films:
#     print(film)
#
# for i in range(len(films)):
#     print(films[i])
#
# index = 0
# while index < len(films):
#     print(films[index])
#     index += 1
#
#
#


# dia 23
# films = ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji']
# print('Before:', films)
#
# for i in range(len(films)):
#     films[i] = films[i].upper()
# print('After:', films)
#
# index = 0
# while index < len(films):
#     films[index] = 'Film ' + str(index + 1)
#     index += 1
# print('After while loop:', films)
#
# dia 26
# teaching_days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
# lesson_hours = (3, 4.5, 6, 4.5, 3)
# lesson_hours_per_day = teaching_days + lesson_hours
# print(lesson_hours_per_day)
#
# print()
# greek_letters = ['alpha', 'beta', 'omega']
# more_letters = greek_letters * 4
# print(more_letters)

#
# dia 30
list_hours_day = ['Mon', 6, 'Tue', 4.5, 'Wed', 3, 'Thu', 0, 'Fri', 4.5]
for item in list_hours_day:
    print(item)
# hours_school_day = [['Mon', 6], ['Tue', 4.5], ['Wed', 3], ['Thu', 0], ['Fri', 4.5]]
#
# print('Day', 'Hours', sep='\t')
# for day in hours_school_day:
#     for item in day:
#         print(item, end='\t')
#     print()

# dia 31
# even_numbers = list(range(2,21,2))
# odd_numbers = tuple(range(1,21,2))
# print(even_numbers)
# print(odd_numbers)
