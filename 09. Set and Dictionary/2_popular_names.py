with open('first_names1ITF.txt') as file1ITF:
    names_list_1ITF = file1ITF.readlines()
with open('first_names2ITF.txt') as file2ITF:        
    names_list_2ITF = file2ITF.readlines()

set_1ITF = set(names_list_1ITF)
set_2ITF = set(names_list_2ITF)

print('In 1ITF there are', len(set_1ITF), 'different first names')
print('In 2ITF there are', len(set_2ITF), 'different first names')

set_popular_names = set_1ITF & set_2ITF
print('These are the', len(set_popular_names), 'first names appearing in both 1ITF and 2ITF')


# Part A
# for popular_name in set_popular_names:
#     print(popular_name.rstrip())

# Part B
sorted_popular_names = sorted(list(set_popular_names))
for popular_name in sorted_popular_names:
    print(popular_name.rstrip())

