import sys

if __name__ == '__main__':
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        line = file.read()

    front = 0
    back = (len(line) - 1) >> 1
    check_sum = 0

    free_space_size = list(map(int, list(line)))[1::2]
    free_start_index = [0] * back
    file_space_size = list(map(int, list(line)))[::2]
    file_start_index = [0] * (back+1)
    free_index = 0
    file_index = 0
    input_index = 0

    result = []
    for i in range(len(line)):
        if i & 1:
            free_start_index[free_index] = input_index
            for _ in range(int(line[i])):
                result.append('.')
            free_index += 1
        else:
            file_start_index[file_index] = input_index
            for _ in range(int(line[i])):
                result.append(file_index)
            file_index += 1

        input_index += int(line[i])

    print(result)
    result = list(result)

    for i in range(len(file_space_size)-1, -1, -1):
        for j in range(len(free_space_size)):
            if i <= j: continue
            if file_space_size[i] <= free_space_size[j]:
                for k in range(file_space_size[i]):
                    result[free_start_index[j]+k] = str(i)
                    result[file_start_index[i]+k] = "."
                free_space_size[j] -= file_space_size[i]
                free_start_index[j] += file_space_size[i]
                break
    for i in range(len(result)):
        if result[i] != '.':
            check_sum += int(result[i])*i

    #8633000799994 is too high
    #6382582136592
    #4181910531650 is too low

    print(check_sum)