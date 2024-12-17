# from typing import List

total_number_certificate = 0
with open('sponsors.txt') as file:
    sponsor_list = file.readlines()
sponsor_list.sort()     #

print("Overview gifts")
print("Number\tSponsor")

i = 0
fields = sponsor_list[i].rstrip().split('*')  # prime read

while i < len(sponsor_list):
    # start new sponsor
    sponsor_ind = fields[0]
    total_per_sponsor = 0
    receive_form = ''
    print(str(sponsor_ind) + "\t" + fields[1] + ' ' + fields[2], end='')

    while i < len(sponsor_list) and fields[0] == sponsor_ind:
        total_per_sponsor += int(fields[3])
        i += 1
        if i < len(sponsor_list):                           # avoid error last line
            fields = sponsor_list[i].rstrip().split('*')    # read again
    # end of sponsor
    if total_per_sponsor >= 40:
        total_number_certificate += 1
        receive_form = "**"
    print('\t' + str(total_per_sponsor) + '\t' + receive_form)
# end of program
print('There are', total_number_certificate, 'tax certificates to be sent.')
