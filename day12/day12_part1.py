def dfs(arr, farm, crop_type, location):
    i = location[0]
    j = location[1]

    if i-1 >= 0 and (i-1, j) not in farm and arr[i-1][j] == crop_type:
        farm.add((i-1, j))
        dfs(arr, farm, crop_type, (i-1, j))
    if j-1 >= 0 and (i, j-1) not in farm and arr[i][j-1] == crop_type:
        farm.add((i, j-1))
        dfs(arr, farm, crop_type, (i, j-1))
    if i+1 < len(arr) and (i+1, j) not in farm and arr[i+1][j] == crop_type:
        farm.add((i+1, j))
        dfs(arr, farm, crop_type, (i+1, j))
    if j+1 < len(arr[0]) and (i, j+1) not in farm and arr[i][j+1] == crop_type:
        farm.add((i, j+1))
        dfs(arr, farm, crop_type, (i, j+1))

def get_perimeter(farm, crop_type):
    perimeter = 0
    for land in farm:
        i = land[0]
        j = land[1]
        if i - 1 == -1 or arr[i - 1][j] != crop_type:
            perimeter+=1
        if j - 1 == -1 or arr[i][j - 1] != crop_type:
            perimeter+=1
        if i + 1 == len(arr) or arr[i + 1][j] != crop_type:
            perimeter+=1
        if j + 1 == len(arr[0]) or arr[i][j + 1] != crop_type:
            perimeter+=1

    return perimeter

if __name__ == '__main__':
    arr = []
    # set that will save visited position as a tuple
    visited = set()
    file = "part1.in"
    # read file, separate characters, save like a 2D array
    with (open(file, 'r') as file):
        for line in file:
            arr.append(list(line[:-1]))

    cost = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if (row, col) not in visited:
                farm = set()
                farm.add((row, col))
                dfs(arr, farm, arr[row][col], (row, col))
                cost += len(farm) * get_perimeter(farm, arr[row][col])
                visited.update(farm)

    print(cost)
