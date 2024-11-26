import random as rd

def convert(amount_in_euro, dollar_rate):
     return amount_in_euro * dollar_rate

#MAIN
rate = float(input('Current dollar rate (€ -> $): '))
amount = float(input('Your amount in Euro: '))
out = convert(amount, rate)
print('€',amount, '= $', out)



