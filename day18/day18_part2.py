import heapq

if __name__ == '__main__':
    arr = [ ['.']*71 for i in range(71)]
    corrupted = set()

    dist = {}
    dist[(0, 0)] = 0
    parent = {}
    pq = []
    heapq.heappush(pq, (0, (0, 0)))
    while pq:
        cost, location = heapq.heappop(pq)
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in direction:
            if not (0 <= location[0] + di < 71 and 0 <= location[1] + dj < 71):
                continue
            if (location[0] + di, location[1] + dj) in corrupted:
                continue
            if (location[0] + di, location[1] + dj) not in dist or cost + 1 < dist[
                (location[0] + di, location[1] + dj)]:
                parent[(location[0] + di, location[1] + dj)] = location
                dist[(location[0] + di, location[1] + dj)] = cost + 1
                heapq.heappush(pq, (cost + 1, (location[0] + di, location[1] + dj)))
    bt = (70, 70)
    while bt != (0, 0):
        arr[bt[0]][bt[1]] = 'O'
        bt = parent[bt]
    # read file
    with (open("real.in", 'r') as file):
        for line in file:
            memory_drop = (int(line[:line.index(',')]), int(line[line.index(',')+1:]))
            if memory_drop in corrupted:
                print(corrupted)
                continue
            corrupted.add(memory_drop)
            if arr[memory_drop[0]][memory_drop[1]] == 'O':
                arr[memory_drop[0]][memory_drop[1]] = '#'
                dist = {}
                dist[(0, 0)] = 0
                parent = {}
                pq = []
                heapq.heappush(pq, (0, (0, 0)))
                while pq:
                    cost, location = heapq.heappop(pq)
                    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for di, dj in direction:
                        if not (0 <= location[0] + di < 71 and 0 <= location[1] + dj < 71):
                            continue
                        if (location[0] + di, location[1] + dj) in corrupted:
                            continue
                        if (location[0] + di, location[1] + dj) not in dist or cost + 1 < dist[
                            (location[0] + di, location[1] + dj)]:
                            parent[(location[0] + di, location[1] + dj)] = location
                            dist[(location[0] + di, location[1] + dj)] = cost + 1
                            heapq.heappush(pq, (cost + 1, (location[0] + di, location[1] + dj)))

                if (70, 70) not in dist:
                    print(memory_drop)
                    break

                for m in arr:
                    m = list(map(lambda x: '.' if x == 'O' else x, m))
                bt = (70,70)
                while bt != (0,0):
                    arr[bt[0]][bt[1]] = 'O'
                    bt = parent[bt]
            arr[memory_drop[0]][memory_drop[1]] = '#'

