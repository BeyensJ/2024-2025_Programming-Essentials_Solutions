a = int(input("Number 1 (0, 1 or 2): "))
b = int(input("Number 2 (0, 1 or 2): "))
c = int(input("Number 3 (0, 1 or 2): "))
result = 0

if a == b and b == c:
    if a == 2:
        result = 10
    else:
        result = 5
elif a != b and a != c:
    result = 1

print(result)
