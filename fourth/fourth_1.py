if __name__ == '__main__':
    count = 0
    arr = []
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        for line in file:
            arr.append(list(line[:-1]))

    #find character X, search for all possible XMAS
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X' :
                #horizontal, forward
                if j <= len(arr[i])-4 and arr[i][j+1] == 'M' and arr[i][j+2] == 'A' and arr[i][j+3] == 'S':
                    count+=1

                #horizontal, backward
                if j >= 3 and arr[i][j-1] == 'M' and arr[i][j-2] == 'A' and arr[i][j-3] == 'S':
                    count += 1

                #vertical, downward
                if i <= len(arr)-4 and arr[i+1][j] == 'M' and arr[i+2][j] == 'A' and arr[i+3][j] == 'S':
                    count+=1

                #vertical, upward
                if i >= 3 and arr[i-1][j] == 'M' and arr[i-2][j] == 'A' and arr[i-3][j] == 'S':
                    count += 1

                #diagonal, 11 o'clock
                if i >= 3 and j >= 3 and arr[i-1][j-1] == 'M' and arr[i-2][j-2] == 'A' and arr[i-3][j-3] == 'S':
                    count += 1

                # diagonal, 1 o'clock
                if i >= 3 and j <= len(arr[i])-4 and arr[i-1][j+1] == 'M' and arr[i-2][j+2] == 'A' and arr[i-3][j+3] == 'S':
                    count += 1

                # diagonal, 5 o'clock
                if i <= len(arr)-4 and j <= len(arr[i])-4 and arr[i+1][j+1] == 'M' and arr[i+2][j+2] == 'A' and arr[i+3][j+3] == 'S':
                    count += 1

                # diagonal, 7 o'clock
                if i <= len(arr)-4 and j >= 3 and arr[i+1][j-1] == 'M' and arr[i+2][j-2] == 'A' and arr[i+3][j-3] == 'S':
                    count += 1
    print(count)