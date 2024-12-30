if __name__ == '__main__':
    count = 0
    arr = []
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        for line in file:
            arr.append(list(line[:-1]))

    #find character A, search for all possible X-MAS
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            if arr[i][j] == 'A' :
                #MMSS
                if arr[i-1][j-1] == 'M' and arr[i-1][j+1] == 'M' and arr[i+1][j-1] == 'S' and arr[i+1][j+1] == 'S' :
                    count += 1

                #SSMM
                if arr[i-1][j-1] == 'S' and arr[i-1][j+1] == 'S' and arr[i+1][j-1] == 'M' and arr[i+1][j+1] == 'M' :
                    count += 1

                #SMSM
                if arr[i-1][j-1] == 'S' and arr[i-1][j+1] == 'M' and arr[i+1][j-1] == 'S' and arr[i+1][j+1] == 'M' :
                    count += 1

                #MSMS
                if arr[i-1][j-1] == 'M' and arr[i-1][j+1] == 'S' and arr[i+1][j-1] == 'M' and arr[i+1][j+1] == 'S' :
                    count += 1

    print(count)