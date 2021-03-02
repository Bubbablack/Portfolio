p = input("please type in some words?")

def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))


frame(p.split(" "))
