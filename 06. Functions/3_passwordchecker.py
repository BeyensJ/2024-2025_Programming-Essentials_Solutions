# FUNCTIONS
def password_checker(password):
    marks = ['!', '#', '$', '%', '&']
    has_upper = False
    has_lower = False
    has_digit = False
    has_marks = False
    result = False

    if len(password) >= 12:
        for char in password:
            if char.isalpha():
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
            elif char in marks:
                has_marks = True
            elif char.isdigit():
                has_digit = True

        if has_upper and has_lower and has_marks and has_digit:
            result = True

    return result

# ASSERTS
assert(password_checker('8&tSD%EmKke$8rs#')) == True
assert(password_checker('agP#9Y0fUo%i')) == True
assert(password_checker('2v$tqj&x$&1qN4ZYgk')) == True
assert(password_checker('kENb#lv77')) == False
assert(password_checker('770xbi#&!n3e')) == False
assert(password_checker('vfJLD!Nt#Ul')) == False

# MAIN PROGRAM
pwd_tocheck = input("Please provide a paswoord to check: ")
while not password_checker(pwd_tocheck):
    print('This password does not meet the criteria.')
    print()
    pwd_tocheck = input("Please provide a new paswoord to check: ")
print('This password is ok!')

