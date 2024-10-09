print("Press Enter for each new striker you see.")
print("If you want to enter a group, enter the number of strikers.")
print("If you want to stop, type 'S' and press Enter.")

strikers = 0
yesno = "N"

while yesno != "y" and yesno != "Y":
    data = input()
    if data == "":
        strikers += 1
    elif data == "S":
        yesno = input("Are you sure you want to stop? (Y/N) ")
    else:    
        strikers += int(data)

print("You saw", strikers, "strikers.")