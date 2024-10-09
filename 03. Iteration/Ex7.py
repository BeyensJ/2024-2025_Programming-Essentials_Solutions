# A
print("sum of the numbers from 25 till 32")
result = 25
for i in range(25,32):
    result += i+1
    print("+", i+1, "-->", result)

# B
initial = int(input("Initial limit"))
final = int(input("Final limit"))
result = initial

if initial > final:
    print("The initial limit muse be smaller than the final limit!")
elif initial == final:
    print(initial)
else:
    for i in range(initial,final):
        result += i+1
        print("+", i+1, "-->", result)

