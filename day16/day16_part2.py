import sys
import heapq
import time
import queue

if __name__ == '__main__':
    arr = []
    # read file
    with (open("real.in", 'r') as file):
        line_number = 0
        for line in file:
            arr.append(list(line[:-1]))
            if line.find('S') != -1:
                start = (line_number, line.index('S'))
                arr[start[0]][start[1]] = '.'
            if line.find('E') != -1:
                end = (line_number, line.index('E'))
                arr[end[0]][end[1]] = '.'
            line_number += 1

    best_score = 2147483647

    def traverse(location, direction, cost):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dd in directions:
            if dd[0] == direction[0]*-1 and dd[1] == direction[1]*-1:
                continue
            if arr[location[0]+dd[0]][location[1]+dd[1]] == '.':
                if dd == direction:
                    yield (location[0]+dd[0], location[1]+dd[1]), cost+1
                else:
                    yield (location[0]+dd[0], location[1]+dd[1]), cost+1001



    parent = {}
    parent[start] = [(start[0], start[1]-1)] # direction = current - parent
    dist = {}
    dist[start] = 0

    pq = []
    # heapq.heappush(pq, (priority, item))
    # priority = cost, item = index tuple
    # heapq.heappop(pq)
    heapq.heappush(pq, (0, start))

    while pq:
        cost, location = heapq.heappop(pq)
        # consider all parent paths
        for para in parent[location]:
            # consider all possible directions
            for new_location, new_distance in traverse(location, (location[0]-para[0], location[1]-para[1]), cost):
                # if this is first time visiting that node
                if new_location not in dist:
                    parent[new_location] = []
                    parent[new_location].append(location)
                    dist[new_location] = new_distance
                    heapq.heappush(pq, (new_distance, new_location))
                # if this isn't first time visiting (not infinite weight)
                elif new_distance == dist[new_location]:
                    parent[new_location].append(location)
                elif new_distance < dist[new_location]:
                    parent[new_location] = []
                    parent[new_location].append(location)
                    dist[new_location] = new_distance
                    heapq.heappush(pq, (dist[new_location], new_location))
        #time.sleep(2)

    q = queue.Queue()
    q.put(end)
    best_path = set()

    # reverse direction = parent - current
    while not q.empty():
        current = q.get()
        best_path.add(current)

        if current == start:
            continue

        for para in parent[current]:
            q.put(para)

            di = current[0] - para[0]
            dj = current[1] - para[1]

            if di == 0:
                if arr[current[0] + 1][current[1]] == '.' and dist[(current[0] + 1, current[1])] - 1000 == dist[para] and arr[current[0] - 1][current[1]] == '.' and dist[(current[0] - 1, current[1])] == dist[para] + 1002:
                    q.put((current[0] + 1, current[1]))
                if arr[current[0] - 1][current[1]] == '.' and dist[(current[0] - 1, current[1])] - 1000 == dist[para] and arr[current[0] + 1][current[1]] == '.' and dist[(current[0] + 1, current[1])] == dist[para] + 1002:
                    q.put((current[0] - 1, current[1]))
            elif dj == 0:
                if arr[current[0]][current[1] + 1] == '.' and dist[(current[0], current[1] + 1)] - 1000 == dist[para] and arr[current[0]][current[1] - 1] == '.' and dist[(current[0], current[1] - 1)] == dist[para] + 1002:
                    q.put((current[0], current[1]+1))
                if arr[current[0]][current[1] - 1] == '.' and dist[(current[0], current[1] - 1)] - 1000 == dist[para] and arr[current[0]][current[1] + 1] == '.' and dist[(current[0], current[1] + 1)] == dist[para] + 1002:
                    q.put((current[0], current[1]-1))


    print(dist[end])
    for i, j in best_path:
        arr[i][j] = 'O'

    print(len(best_path))
    f = open("real.out", "w")
    for i in arr:
        f.write("".join(i))
        f.write("\n")
    f.close()