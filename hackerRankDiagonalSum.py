n = int(input())

for _ in range(n):
    t = int(input())
    j = t-1
    ls = list(map(int, input().split()))
    c = 0
    for i in reversed(ls):

        if i != 0:
            c = j
            break

        j -= 1

    print(c)

