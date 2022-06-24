string = "heeymynameis"
k = 3
string3 = ""

chunks = [string[i:i+k] for i in range(0, len(string), k)]

# print(chunks)

string2 = []

for i in chunks:
    # print(i)

    for j in i:

        if j not in string2:
            string2.append(j)

    string2.append(":")

for i in string2:

    string3 += i

lst3 = string3.split(':')

for i in lst3:
    print(i)

# print(lst3)

