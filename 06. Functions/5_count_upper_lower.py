def count(string):
    result = [0, 0]
    for letter in string:
        if letter.isupper():
            result[0] += 1
        elif letter.islower():
            result[1] += 1
    return result

# text = input("Your string: ")
# result_count = count(text)
# print("Number of capitals:", result_count[0])
# print("Number of lowercase letters:", result_count[1])

password = input('Set your password (at least 2 uppercase and 3 lowercase letters): ')
result_count = count(password)
while result_count[0] < 2 or result_count[1] < 3:
    password = input('Set your password (at least 2 uppercase and 3 lowercase letters): ')
    result_count = count(password)
