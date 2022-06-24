t = int(input())

for _ in range(t):
    n = int(input())
    # n = input()
    ls = set(map(int, input().split()))
    powerSet = set({})
    count = 0

    for i in ls:
        if i != 0:
            flag = 1
        else:
            flag = 0

    if flag == 1:
        for i in ls:
            for j in range(1, 100):
                if i % 2 ** j == 0:
                    powerSet.add(i)
                    count += 1
                    # ls.remove(i)
                    break

        for i in ls:
            temp1 = i
            # temp = 0

            while temp1 != 0:

                for j in range(1, 100):

                    if 2 ** j > temp1:
                        # print("hy")

                        temp = 2 ** (j - 1)
                        # print(temp, temp1)

                        temp1 -= temp
                        break

                if temp not in powerSet:
                    count += 1
                    break
                else:
                    break

            # for j in range(len(powerSet)):
            #
            #     while i != 0:
            #         if i < powerSet[j]:
            #             i -= powerSet[j-1]

        # print(ls)
        print(count)
        # print(powerSet)
    else:
        print(0)
# print("hy")
