day = (input('Enter the current day: '))

# Interpreting entry
match day:
    case "Monday":
        print("This is a weekday. It is the 1st day of the week")
    case "Tuesday":
        print("This is a weekday. It is the 2nd day of the week")
    case "Wednesday":
        print("This is a weekday. It is the 3rd day of the week")
    case "Thursday":
        print("This is a weekday. It is the 4th day of the week")
    case "Friday":
        print("This is a weekday. It is the 5th day of the week")
    case "Saturday":
        print("This is a weekend day. It is the 6th day of the week")
    case "Sunday":
        print("This is a weekend day. It is the 7th day of the week")
    case _:
        print("Invalid entry")

