text = input('Enter a string: ')
new_text = ''

i = 0
while i < len(text)-2: #Not till the end because you take them 3 by 3
    new_text += text[i+1]
    new_text += text[i+2]
    new_text += text[i]
    i += 3 #take the next three characters

new_text += text[i:] #add last characters
print(new_text)

# or
# text = input('Give a string: ')
# new_text = ''

# for i in range(0,len(text)-2,3): #Not till the end because you take them 3 by 3
#      new_text += text[i+1]
#      new_text += text[i+2]
#      new_text += text[i]

# surplus = len(text) % 3

# Add last characters
# new_text += text[i:]
# if surplus > 0:
#      print(new_text + text[-surplus:])
# else:
#      print(new_text)

