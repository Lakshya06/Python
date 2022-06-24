t = int(input())

for _ in range(t):
    # print(i)
    n, m = map(int, input().split())
    ls1 = list(map(int, input().split()))

    a = max(ls1)
    res = 0

    for b in ls1:

        t1 = (a+b) + (a-b) % m
        t2 = (a+b) + (b-a) % m
        # print("a=", a)
        # print("b=", b)
        # print("t1=",t1)
        # print("t2",t2)
        res = max(t1, t2, res)

    print(res)
# print(ls1[0])
