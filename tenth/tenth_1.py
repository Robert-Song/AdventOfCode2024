def recur_dfs(topomap, path, goal, height, location):
    path.add(location)
    if height == 9:
        goal.add(location)
        return
    i = location[0]
    j = location[1]

    if i-1 >= 0 and topomap[i-1][j] == height+1 and (i-1, j) not in path:
        recur_dfs(topomap, path, goal, height+1, (i-1, j))

    if j-1 >= 0 and topomap[i][j-1] == height+1 and (i, j-1) not in path:
        recur_dfs(topomap, path, goal, height+1, (i, j-1))

    if i+1 < len(topomap) and topomap[i+1][j] == height+1 and (i+1, j) not in path:
        recur_dfs(topomap, path, goal, height+1, (i+1, j))

    if j+1 < len(topomap[0]) and topomap[i][j+1] == height+1 and (i, j+1) not in path:
        recur_dfs(topomap, path, goal, height+1, (i, j+1))

if __name__ == '__main__':
    arr = []
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        for line in file:
            arr.append(list(map(int, list(line[:-1]))))

    score = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == 0:
                path = {(-1, -1)}
                goal = {(-1, -1)}
                recur_dfs(arr, path, goal, 0, (row, col))
                score = score + len(goal) - 1
                print(goal)

    print(score)