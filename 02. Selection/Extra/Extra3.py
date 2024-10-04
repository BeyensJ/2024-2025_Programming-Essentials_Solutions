input_char = input("Enter a letter: ")

match input_char:
    case "A":
        print("vowel")
    case "a":
        print("vowel")
    case "E":
        print("vowel")
    case "e":
        print("vowel")
    case "I":
        print("vowel")
    case "i":
        print("vowel")
    case "O":
        print("vowel")
    case "o":
        print("vowel")
    case "U":
        print("vowel")
    case "u":
        print("vowel")
    case "Y":
        print("exception")
    case "y":
        print("exception")
    case _:
        print("consonant")