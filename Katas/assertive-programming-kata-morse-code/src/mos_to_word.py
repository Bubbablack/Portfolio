from dictionary import dic

def decode(temp):
    final = ""
    for key in dic:
        if temp == dic[key]:
            final += key
    return(final)  


def morse_code_to_letters(code):
    temp = ""
    full = ""
    for ch in code:
        if ch == ".":
            temp += "."
        elif ch == "-":
            temp += "-"
        elif ch == "/":
            temp += "/"
        elif ch == " ":
            full += decode(temp)
            temp = ""
    full += decode(temp)

    return(full)

code= input("enter your mos code here")
message = morse_code_to_letters(code)

assert len(code.split()) == len(message)
assert code.count('/') == message.count(" ")

print(message)