text = input('Enter a text: ')
largest = 1
length = 1

for i in range(len(text)-1):
     if text[i] == text[i+1]:
        length += 1
     else:
        length = 1
     if length > largest:
         largest = length

print('The length of the largest block in this text is', largest)