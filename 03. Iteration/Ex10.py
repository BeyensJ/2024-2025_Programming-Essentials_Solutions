for i in range(4):
    print("Information for member", i+1)
    name= input("Name: ")
    age = int(input("Age: "))
    member_for = int(input("Member for how many years: "))
    
    if age < 12:
        fee = 20
    elif age < 18:
        fee = 50
    else :
        fee = 95

    if member_for >= 5:
        fee = fee - fee*0.1

    print("Member fee for", name, "=", fee, end="\n\n")
