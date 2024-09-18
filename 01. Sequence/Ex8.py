current_hour = int(input("Enter the current hour: "))
wait_time = int(input("How long do you want to wait: "))

print("The alarm will sound at " + str((current_hour + wait_time) % 24) + "h.")
