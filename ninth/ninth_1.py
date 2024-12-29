import sys

if __name__ == '__main__':
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        line = file.read()

    front = 0
    back = (len(line) - 1) >> 1
    check_sum = 0

    file_id = [0] * (back + 1)
    file_size = 0
    id_index = 0

    for i in line[::2]:
        file_size = file_size + int(i)
        file_id[id_index] = int(i)
        id_index = id_index + 1

    file_index = 0

    for i in range(len(line)):
        if i & 1:#end
            for j in range(int(line[i])):
                if file_index == file_size:
                    print(check_sum)
                    print(file_id)
                    sys.exit(0)
                if file_id[back] == 0:
                    back = back - 1
                check_sum += file_index * back
                file_index += 1
                file_id[back] = file_id[back] - 1
        else:
            for j in range(int(line[i])):
                if file_index == file_size:
                    print(check_sum)
                    print(file_id)
                    sys.exit(0)
                if file_id[front] == 0:
                    front += 1
                check_sum += file_index * front
                file_index += 1
                file_id[front] -= 1



    print(file_id)
    print(line)

