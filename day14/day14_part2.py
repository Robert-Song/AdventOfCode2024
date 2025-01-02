import time as tm
if __name__ == '__main__':
    arr = []

    file_name = "real"
    file_name += ".in"
    # read file
    with (open(file_name, 'r') as file):
        for line in file:
            arr.append( list(map(int, line[(line.index('p') + 2):line.index('v') - 1].split(','))) + list(map(int, line[(line.index('v') + 2):].split(','))) )
    width = 101
    height = 103

    time = 100

    #184
    #285
    for time_now in range(184, 9999, 101):
        tm.sleep(0.5)

        picture = set()
        frame = []

        for _ in range(height) :
            frame.append([0] * width)




        for i in arr:
            x = (i[0] + time_now*i[2]) % width
            y = (i[1] + time_now*i[3]) % height
            frame[y][x] = 1

        print("-------------------------------------------------------")
        print("time =", time_now)
        for i in range(height):
            for j in range(width):
                if frame[i][j] == 0:
                    print(' ', end='')
                else:
                    print(frame[i][j], end='')
            print()
        print("-------------------------------------------------------")




