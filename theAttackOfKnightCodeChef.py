
def knightMoves(p, q):

    X = [2, 1, -1, -2, -2, -1, 1, 2]
    Y = [1, 2, 2, 1, -1, -2, -2, -1]

    ls = [0, 0]
    res = []

    count = 0
    p, q = 3, 4

    for i in range(8):

        x = p + X[i]
        y = q + Y[i]

        if x >= 0 and y >= 0 and x < 8 and y < 8:
            ls[0] = x
            ls[1] = y
            # print(ls)
            res.append(ls[:])
            # print(res)

    return res


if __name__ == '__main__':

    # moves = knightMoves(3, 4)
    #
    # print(moves)

    t = int(input())

    for _ in range(t):

        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())

        moves1 = knightMoves(x1, y1)
        moves2 = knightMoves(x2, y2)

        for i in range(len(moves1)):
            if moves1[i] == moves2[i]:
                flag = 1
                break

        if flag==1:
            print("YES")
        else:
            print("NO")



