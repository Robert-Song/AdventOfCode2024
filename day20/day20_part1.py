from collections import Counter

if __name__ == '__main__':
    arr = []
    file = "real.in"
    # read file, separate characters, save like a 2D array
    with (open(file, 'r') as file):
        linenum = 0
        for line in file:
            arr.append(list(line))

            if line.find('S') != -1:
                start = (linenum, line.index('S'))
                arr[start[0]][start[1]] = '.'

            if line.find('E') != -1:
                end = (linenum, line.index('E'))
                arr[end[0]][end[1]] = '.'

            linenum += 1

    print(start, end)

    current = start
    track = 0

    dist = {}
    path = []
    while current != end:
        path.append(current)

        dist[current] = track
        arr[current[0]][current[1]] = 'O'
        track+=1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for direction in directions:
            if arr[current[0] + direction[0]][current[1] + direction[1]] == '.':
                current = (current[0] + direction[0], current[1] + direction[1])
                break

    dist[end] = track
    arr[end[0]][end[1]] = 'O'

    result = Counter()

    for current in path:
        directions = [(-2, 0), (0, 2), (2, 0), (0, -2)]
        for direction in directions:
            if not (0<=current[0] + direction[0]<len(arr) and 0<=current[1] + direction[1]<=len(arr[0]) ):
                continue
            if arr[current[0] + direction[0]][current[1] + direction[1]] == 'O':
                saved = dist[(current[0] + direction[0], current[1] + direction[1])] - dist[current]
                if saved > 101:
                    result[saved-2] += 1

    print(sum(result.values()))
