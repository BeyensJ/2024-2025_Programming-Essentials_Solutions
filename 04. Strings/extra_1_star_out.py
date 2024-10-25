proverb = "A barking dog, never bites."
al_gegokt = ",.:!? ed"

for i in proverb:
    if i in al_gegokt:
        print(i, end="")
    else:
        print("#", end="")