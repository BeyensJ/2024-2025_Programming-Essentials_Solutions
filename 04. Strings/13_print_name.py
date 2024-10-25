
name = input("Enter a name: ")

while name != "":
    print(f"\nMenu:\n{len("Menu:")*'-'}")
    print("U uppercase\nL lowercase\nA Alternate")
    choice = input("Make a choice (U - L - A): ")
    while choice not in "UuLlAa":
        choice = input("Make a choice (U - L - A): ")
    
    if choice in "Uu":
        print(name.upper())
    elif choice in "Ll":
        print(name.lower())
    else:
        out = ""
        for i in range(len(name)):
            if i % 2 == 0:
                out += name[i].upper()
            else:
                out += name[i].lower()
        print(out)
        
    name = input("Enter a name: ")