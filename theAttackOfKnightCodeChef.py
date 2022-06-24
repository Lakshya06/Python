
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

    moves = knightMoves(3, 4)

    print(moves)

