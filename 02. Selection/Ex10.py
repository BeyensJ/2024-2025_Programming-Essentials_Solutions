integer1 = int(input("First number: "))
integer2 = int(input("Second number: "))
integer1_ok = False
integer2_ok = False

if ((30 <= integer1 <= 40) or integer1 == 65 or integer1 == 72 or integer1 == 83 or integer1 == 90) and ((30 <= integer2 <= 40) or integer2 == 65 or integer2 == 72 or integer2 == 83 or integer2 == 90):
    print("Both numbers are ok")
else:
    print("They are NOT ok")


