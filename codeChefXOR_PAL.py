t = int(input())

for i in range(t):
    n = int(input())
    ls = list(map(str, input().split()))[:n]
    s = ''.join(ls)
    k = 0

    for j in range(n//2):
        if s[j] != s[n-j-1]:
            k = k + 1

    print((k+1)//2)
