exchange_rate = float(input("Enter the current exchange dollar rate (€ -> $): "))
amount_in_euro = float(input("Enter your amount in euro: "))

print(str(amount_in_euro) + " € = " + str(amount_in_euro * exchange_rate) + " $")
