months = dict(January=31, February=28, March=31,
              April=30, May=31, June=30,
              July=31, August=31, September=30,
              October=31, November=30, December=31)
print(*months)
input_month = input('Month (enter = overview): ')

if input_month in months:
    print(months[input_month])
elif input_month == '':
    for month in months:
        print(month, '\t' , months[month])
else:
    print('This month does not exist.')
