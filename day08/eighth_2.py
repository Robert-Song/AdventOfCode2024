if __name__ == '__main__':
    frequency = {'.'}
    antinodes = {(-1, -1)}
    arr = []
    # read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        for line in file:
            frequency.update(line[:-1])
            arr.append(list(line[:-1]))

    frequency.remove('.')
    frequency_list = []

    # for each freq
    for freq in frequency:
        # build list with all locations of that freq
        frequency_list.clear()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == freq:
                    frequency_list.append((i, j))

        for i in range(len(frequency_list)):
            for j in range(i + 1, len(frequency_list)):
                a = frequency_list[i]
                b = frequency_list[j]
                x = a[1] - b[1]
                y = a[0] - b[0]
                # a+y,x b-y

                a_temp = (a[0], a[1])
                b_temp = (b[0], b[1]    )

                while 0 <= a_temp[0] < len(arr) and 0 <= a_temp[1] < len(arr[a_temp[0]]):
                    if a_temp not in antinodes:
                        antinodes.add(a_temp)
                    a_temp = (a_temp[0] + y, a_temp[1] + x)

                while 0 <= b_temp[0] < len(arr) and 0 <= b_temp[1] < len(arr[b_temp[0]]):
                    if b_temp not in antinodes:
                        antinodes.add(b_temp)
                    b_temp = (b_temp[0] - y, b_temp[1] - x)

    # 252 too low, 263 too high
    print(sorted(antinodes))
    print(len(antinodes) - 1)
    #783 -> 898

