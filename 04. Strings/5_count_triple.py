text = input('Enter a text: ')
number_of_triples = 0

for i in range(len(text) - 2):
    # if text[i] == text[i+1] and text[i] == text[i+2]:
    # if text[i] == text[i+1] == text[i+2]:
    if text[i]*3 == text[i:i+3]:
        number_of_triples += 1

if number_of_triples == 0:
    print ('There are no triples in this text')
elif number_of_triples == 1:
    print ('There is 1 triple in this text')
else:
    print('There are', number_of_triples, 'triples in this text')