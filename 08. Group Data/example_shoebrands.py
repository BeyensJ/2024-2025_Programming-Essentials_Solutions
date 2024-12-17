with open('brand_names.txt') as file:
    number_of_brands = 0
    line = file.readline().rstrip()     #verwijder \n

    while line:
        brandind = line[0]
        print("**", brandind, "**")
        while line and line[0] == brandind:
            number_of_brands += 1
            print(line)
            line = file.readline().rstrip()
        print()

print("Number of shoe brands:", number_of_brands)