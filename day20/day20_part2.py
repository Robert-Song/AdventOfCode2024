import heapq
from collections import Counter

if __name__ == '__main__':
    arr = []
    file = "test.in"
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
    print(dist[end])

    for current in path:
        if dist[current] >= 9480 - 100:
            break

        # key: end location, value: saved time
        duplicate = {}

        dijkstra = {current: 0}
        pq = []
        heapq.heappush(pq, (0, current))

        while pq:
            cost, location = heapq.heappop(pq)
            if cost >= 20:
                break
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in direction:
                if not (0 <= location[0] + di < len(arr) and 0 <= location[1] + dj < len(arr[0])):
                    continue

                if arr[location[0] + di][location[1] + dj] == '#':
                    if (location[0] + di, location[1] + dj) not in dijkstra or cost + 1 < dijkstra[(location[0] + di, location[1] + dj)]:
                        dijkstra[(location[0] + di, location[1] + dj)] = cost + 1
                        heapq.heappush(pq, (cost + 1, (location[0] + di, location[1] + dj)))

                elif arr[location[0] + di][location[1] + dj] == 'O':
                    saved = dist[(location[0] + di, location[1] + dj)] - dist[current] - cost - 1

                    if saved < 50:
                        continue

                    if (location[0] + di, location[1] + dj) in duplicate:
                        if duplicate[(location[0] + di, location[1] + dj)] < saved:
                            result[duplicate[(location[0] + di, location[1] + dj)]] -= 1
                            result[saved] += 1
                            duplicate[(location[0] + di, location[1] + dj)] = saved
                    else:
                        duplicate[(location[0] + di, location[1] + dj)] = saved
                        result[saved] += 1
        print(current, duplicate)

    print(result)
