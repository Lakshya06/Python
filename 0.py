def mutate_string(string, position, character):

    lst = []

    for j in string:
        lst.append(j)

    # d = lst.pop(character)
    lst[position] = character
    print(lst)

    finalString = ""

    for j in lst:
        finalString += j

    return finalString


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
