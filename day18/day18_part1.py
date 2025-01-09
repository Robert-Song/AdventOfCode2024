import heapq

if __name__ == '__main__':
    arr = [ ['.']*71 for i in range(71)]
    corrupted = set()

    line_num = 0
    # read file
    with (open("real.in", 'r') as file):
        for line in file:
            if line_num == 1024:
                break
            corrupted.add( (int(line[:line.index(',')]), int(line[line.index(',')+1:])) )
            line_num += 1

    dist = {}
    dist[(0, 0)] = 0

    pq = []
    # heapq.heappush(pq, (priority, item))
    # priority = cost, item = index tuple
    # heapq.heappop(pq)
    heapq.heappush(pq, (0, (0, 0)))

    while pq:
        cost, location = heapq.heappop(pq)

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in direction:
            if not ( 0<=location[0]+di<71 and 0<=location[1]+dj<71 ):
                continue

            if (location[0]+di, location[1]+dj) in corrupted:
                continue

            if (location[0]+di, location[1]+dj) not in dist or cost+1 < dist[(location[0]+di, location[1]+dj)]:
                dist[(location[0]+di, location[1]+dj)] = cost + 1
                heapq.heappush(pq, (cost+1, (location[0]+di, location[1]+dj)))

    print(dist)
    print(dist[(70, 70)])


