def recur_dfs(topomap, height, location):
    if height == 9:
        return 1
    i = location[0]
    j = location[1]

    temp_sum = 0
    if i-1 >= 0 and topomap[i-1][j] == height+1:
        temp_sum += recur_dfs(topomap, height+1, (i-1, j))

    if j-1 >= 0 and topomap[i][j-1] == height+1 and (i, j-1):
        temp_sum += recur_dfs(topomap, height+1, (i, j-1))

    if i+1 < len(topomap) and topomap[i+1][j] == height+1 and (i+1, j):
        temp_sum += recur_dfs(topomap, height+1, (i+1, j))

    if j+1 < len(topomap[0]) and topomap[i][j+1] == height+1 and (i, j+1):
        temp_sum += recur_dfs(topomap, height+1, (i, j+1))

    return temp_sum

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
                score += recur_dfs(arr, 0, (row, col))


    print(score)
    #566