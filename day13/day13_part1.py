import numpy as np

if __name__ == '__main__':
    arr = []
    temp = []
    file_name = "real"
    file_name += ".in"
    flush = 0
    # read file
    with (open(file_name, 'r') as file):
        for line in file:
            if flush == 3:
                flush = 0
                arr.append(temp.copy())
                temp = []
                continue
            temp.append( (int(line[(line.index('X')+2):line.index('Y')-2]), int(line[line.index('Y')+2:])) )
            flush += 1

    parallel_count = 0
    coin = 0
    # A cost 3 and B cost 1
    for i in arr:
        # parallel or same
        aX = i[0][0]
        aY = i[0][1]
        bX = i[1][0]
        bY = i[1][1]
        goalX = i[2][0]
        goalY = i[2][1]
        '''
        if aX / bX == aY / bY:
            print("yes, we have that case.")
            parallel_count += 1
            continue
            if aX / aY == goalX / goalY:
                # same lines
                if aX < bX:
                    if goalX % aX == 0 and goalY % aY == 0:
                        # TODO: find minimum cost for this case
                        if aX / bX > 3:
                            print("test")

                    else:
                        continue
                else:
                    if goalX % bX == 0 and goalY % aY == 0:
                        # TODO: find minimum cost for this case
                        print("Test")
                    else:
                        continue
            else:
                # parallel lines
                continue
        
        else:
        '''
        left = np.array([[aX, bX], [aY, bY]])
        right = np.array([goalX, goalY])
        sol = np.linalg.solve(left, right)

        if abs(sol[0] - round(sol[0])) > 0.001 or (sol[1] - round(sol[1])) > 0.001 :
            continue

        if sol[0] > 100 or sol[1] > 100 or sol[0] < 0  or sol[1] < 0:
            continue

        print(sol)
        coin += 3*sol[0] + sol[1]

    print(coin)