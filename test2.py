n = int(input())
ls = list([])

for _ in range(n):

    lsSize = int(input())
    ls = list(map(int, input().split()))

    if lsSize > 1:

        for i in range(lsSize):
            if i == 0:
                if ls[i] == ls[i+1]:
                    del ls[i]

            elif i == lsSize-1:
                if ls[i] == ls[lsSize-2]:
                    del ls[i]
            else:
                if ls[i] == ls[i - 1] or ls[i] == ls[i + 1]:
                    del ls[i]

    print(len(list(ls)))
# cook your dish here
