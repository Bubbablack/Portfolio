from dictionary import dic


def letters_to_morse_code(word):
    final = ""
    word = word.lower()
    for ch in word:
        for key in dic:
            if ch == key:
                final += dic[key]
                final += " "
    final.rstrip()  
 
    return(final)  

word = input('enter your text here ')
message = letters_to_morse_code(word)

assert len(word) == len(message.split())
assert word.count(" ") == message.count("/")

print(message)

