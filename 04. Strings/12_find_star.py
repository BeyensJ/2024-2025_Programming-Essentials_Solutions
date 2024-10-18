def method_1(text):
    while text.find('*') != -1:
        if text.find('*') == 0:
            text = text[2:]
        else:
            text = text[:text.find('*')-1] + text[text.find('*')+2:]
            
    return(text)

assert method_1("abc*def") == "abef"
assert method_1("*def") == "ef"
assert method_1("def*") == "de"
assert method_1("a*cde*gf") == "df"


def method_2(text):
    out = ""
    for i in range(len(text)):
        if i == 0:
            if "*" not in text[:2]:
                out += text[i]
        elif "*" not in text[i-1:i+2]:
            out += text[i]
            
    return(out)

# print(method_2( input("Enter a string: ")))
assert method_2("abc*def") == "abef"
assert method_2("*def") == "ef"
assert method_2("def*") == "de"
assert method_2("a*cde*gf") == "df"

def method_3(text):
    out = ""
    next_out = False
    for i in range(len(text)):
        if text[i] == "*":
            out = out[:-1]
            next_out = True
        elif not next_out:
            out += text[i]
        else:
            next_out = False
    return(out)

# print(method_3( input("Enter a string: ")))
assert method_3("abc*def") == "abef"
assert method_3("*def") == "ef"
assert method_3("def*") == "de"
assert method_3("a*cde*gf") == "df"


