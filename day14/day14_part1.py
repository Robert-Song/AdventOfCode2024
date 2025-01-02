if __name__ == '__main__':
    arr = []

    file_name = "real"
    file_name += ".in"
    # read file
    with (open(file_name, 'r') as file):
        for line in file:
            arr.append( list(map(int, line[(line.index('p') + 2):line.index('v') - 1].split(','))) + list(map(int, line[(line.index('v') + 2):].split(','))) )

    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0

    width = 101
    height = 103

    for i in arr:
        x = (i[0] + 100*i[2]) % width
        y = (i[1] + 100*i[3]) % height
        if 0 <= x < width >> 1 and 0 <= y < height >> 1:
            quad1 += 1
            continue
        if width >> 1 < x and 0 <= y < height >> 1:
            quad2 += 1
            continue
        if width >> 1 < x and height >> 1 < y:
            quad3 += 1
            continue
        if 0 <= x < width >> 1 and height >> 1 < y:
            quad4 += 1
            continue

    print(quad1 * quad2 * quad3 * quad4)
