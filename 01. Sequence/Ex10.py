day_consumption = int(input("Power consumption during the day (kilowatt per hour): "))
night_consumption = int(input("Power consumption at night (kilowatt per hour): "))
fixed_costs = 83.6
day_costs = day_consumption * 0.146
night_costs = night_consumption * 0.073
total_excluding_vat = fixed_costs + day_costs + night_costs
total_including_vat = total_excluding_vat * 1.06

print("Invoice\n*******")
print("Fixed costs: €" + str(fixed_costs))
print("Daily consumption: €" + str(day_costs))
print("Night consumption: €" + str(night_costs))
print("Total excluding VAT: €" + str(total_excluding_vat))
print("Total including VAT: €" + str(total_including_vat))