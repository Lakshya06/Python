str = "Hello 10"
finalstr = ""

for i in str:
    a = i

    print(type(a))

    if a.isupper():
        a = a.lower()
        finalstr += a

    elif a.islower():
        a = a.upper()
        finalstr += a

    else:
        finalstr += a

print(finalstr)