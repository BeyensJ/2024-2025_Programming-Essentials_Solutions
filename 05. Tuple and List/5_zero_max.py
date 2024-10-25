numbers = [42, 18, 0, 37, 0, 2, 19, 10, 5, 14]
# numbers = [42, 18, 17, 0, 2, 19, 0]

print(numbers)

for index in range(len(numbers)-1):
    if numbers[index] == 0:
        #loop to look for the largest odd number to the right of the current 0
        largest_odd = 0
        for i in range(index+1,len(numbers)):
            if numbers[i] % 2 != 0 and numbers[i] > largest_odd :
                largest_odd = numbers[i]
        numbers[index] = largest_odd
print(numbers)
