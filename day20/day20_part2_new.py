import heapq
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

    ctr = Counter()

    for current in path:
        if dist[end] - dist[current] < 100:
            break
        duplicate = {}
        for di in range(-20, 21):
            for dj in range(-20, 21):
                if abs(di)+abs(dj) > 20:
                    continue
                if not (0 < current[0]+di < len(arr) and 0 < current[1]+dj < len(arr[0]) ):
                    continue
                if arr[current[0]+di][current[1]+dj] == '#':
                    continue
                if arr[current[0]+di][current[1]+dj] == 'O':
                    saved = dist[(current[0]+di, current[1]+dj)] - dist[current] - abs(di) - abs(dj)

                    if saved < 100:
                        continue

                    if (current[0]+di, current[1]+dj) not in duplicate:
                        ctr[saved] += 1
                        duplicate[(current[0]+di, current[1]+dj)] = saved

                    elif duplicate[(current[0]+di, current[1]+dj)] < saved:
                        ctr[duplicate[(current[0]+di, current[1]+dj)]] -= 1
                        ctr[saved] += 1
                        duplicate[(current[0]+di, current[1]+dj)] = saved

    print(sum(ctr.values()))

