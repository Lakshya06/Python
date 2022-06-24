def knightMoves(p, q):
    
    # print("p=", p)
    # print("q= ", q)

    X = [2, 1, -1, -2, -2, -1, 1, 2]
    Y = [1, 2, 2, 1, -1, -2, -2, -1]

    ls = [0, 0]
    res = []
    res.clear()

    count = 0
    # p, q = 3, 4

    for i in range(8):
        
        x = p + X[i]
        y = q + Y[i]

        if x >= 0 and y >= 0 and x < 8 and y < 8:
            ls[0] = x
            ls[1] = y
            # print(ls)
            res.append(ls[:])
            # print(res)
            
    # print(res)

    return res


if __name__ == '__main__':

    flag = 0

    # moves = knightMoves(3, 4)
    #
    # print(moves)

    t = int(input())

    for _ in range(t):

        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        
        # print(x1, y1)
        # print(x2, y2)

        moves1 = knightMoves(x1, y1)
        moves2 = knightMoves(x2, y2)
        
        print("m1=", moves1)
        print("m2=", moves2)

        # for i in range(len(moves1)-1):
        #     for j in moves1[i]:
        #         if j == 0:
        #             del moves1[i]
         
        # for i in range(len(moves2)-1):
        #     for j in moves2[i]:
        #         if j == 0:
        #             del moves2[i]           
        
        # print(moves1)
        # print(moves2)

        # for i in range(len(moves1)):
        #     if moves1[i] == moves2[i]:
        #         flag = 1
        #         break
        
        for i in moves1:
            
            if i in moves2:
                
                for j in i:
                    if j == 0:
                        continue
                # print("i=", i)
                flag = 1
                break
            
            else:
                flag = 0

        if flag==1:
            print("YES")
        else:
            print("NO")
