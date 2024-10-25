numbers = (4, 3, 7, 5, 1, 3, 8, 4)
print(numbers)

if 4 not in numbers:
    print('The number 4 does not appear in the Tuple')
else:
    # oplossing klopt niet: toont alles vanaf de eerste vier, niet vanaf de laatste
    # location = numbers.index(4)
    # new = numbers[location+1:]
    # print(new)
    while 4 in numbers:
        location = numbers.index(4)
        numbers = numbers[location+1:]
    print(numbers)

    
## Another possibility:
# numbers = (4, 2, 3, 9, 1, 4)
# print(numbers)
# found = False
# index = len(numbers)
# while not found and index > 0:
#     index -= 1
#     if numbers[index] == 4:
#         found = True
#
# if not found:
#     print ('The number 4 does not appear in the Tuple')
# else:
#     partNumbers = numbers[index+1:len(numbers)]
#     print(partNumbers)

## Another possibility:
# numbers = (2, 3, 7, 5, 4, 1, 9, 8)
# print(numbers)
#
# if 4 not in numbers:
#      print('The number 4 does not appear in the Tuple')
# else:
#      found = False
#      index = len(numbers)
#      while not found and index > 0:
#          index -= 1
#          if numbers[index] == 4:
#              found = True
#      partNumbers = numbers[index + 1:len(numbers)]
#      print(partNumbers)

## Another option:
# numbers = (4, 2, 3, 7, 4, 1, 3, 4, 7, 8, 3)
# print(numbers)
# print("len = ", len(numbers))
# index = -1

# #Loop trough list, store index of digit if == 4 --> index is always overwriting
# for i in range(len(numbers)):
    # if numbers[i] == 4:
        # index = i

# #if index is still -1 --> no 4 in list
# if index == -1:
    # print('The number 4 does not appear in the Tuple')
# #slice input list starting from the item next to last "4" until the end
# else:
    # numbers = numbers[index + 1:]
    # print(numbers)
    
## Another possibility:
# if 4 not in numbers:
#     print('The number 4 does not appear in the Tuple')
# else:
#     numbers = list(numbers)
#     numbers.reverse()
#     numbers = numbers[:numbers.index(4)+1]
#     numbers.reverse()
#     print(tuple(numbers))