voted_yes = int(input("How many voted YES: "))
voted_no = int(input("How many voted NO: "))
voted_blank = int(input("Number of blank votes: "))

total_votes = voted_blank + voted_no + voted_yes

print("YES: " + str(voted_yes / total_votes * 100) + "%")
print("NO: " + str(voted_no / total_votes * 100) + "%")
print("Blank: " + str(voted_blank / total_votes * 100) + "%")

# print("YES:", (voted_yes / total_votes * 100), "%")
# Would have been fine, but there is a space between the number and the percentage sign, which makes it wrong.