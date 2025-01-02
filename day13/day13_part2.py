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
            temp.append((int(line[(line.index('X') + 2):line.index('Y') - 2]), int(line[line.index('Y') + 2:])))
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
        goalX = i[2][0]+10000000000000
        goalY = i[2][1]+10000000000000


        bX = bX / aX
        goalX = goalX / aX
        aX = 1

        bY = bY - (bX * aY)
        goalY = goalY - (goalX * aY)
        aY = 0

        goalY = goalY / bY
        goalX = goalX - (goalY * bX)

        if round(goalX) < 0 or round(goalY) < 0 or abs(goalX - round(goalX)) > 0.01 or abs(goalY - round(goalY)) > 0.01:
            continue

        else:
            coin += 3 * round(goalX) + round(goalY)

    #92827349540204
    print(coin)