if __name__ == '__main__':
    frequency = {'.'}
    antinodes = {(-1, -1)}
    arr = []
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        for line in file:
            frequency.update(line[:-1])
            arr.append(list(line[:-1]))

    frequency.remove('.')
    frequency_list = []

    #for each freq
    for freq in frequency:
        #build list with all locations of that freq
        frequency_list.clear()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == freq:
                    frequency_list.append((i, j))

        for i in range(len(frequency_list)):
            for j in range(i+1, len(frequency_list)):
                a = frequency_list[i]
                b = frequency_list[j]
                x = a[1] - b[1]
                y = a[0] - b[0]
                # a+y,x b-y,x
                if 0 <= a[0] + y < len(arr) and 0<= a[1] + x < len(arr[a[0]]) and (a[0] + y, a[1] + x) not in antinodes:
                    antinodes.add((a[0] + y, a[1] + x))
                if 0 <= b[0] - y < len(arr) and 0<= b[1] - x< len(arr[b[0]]) and (b[0] - y, b[1] - x) not in antinodes:
                    antinodes.add((b[0] - y, b[1] - x))


    #252 too low, 263 too high
    print(antinodes)
    print(len(antinodes) - 1)

