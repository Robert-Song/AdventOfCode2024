import sys


def move(position, direction):
    i = position[0] + direction[0]
    j = position[1] + direction[1]
    item_count = 0
    while arr[i][j] == 'O':
        item_count += 1
        i = i + direction[0]
        j = j + direction[1]

    if arr[i][j] == '#':
        return position

    if arr[i][j] == '.':
        if item_count > 0:
            arr[i][j] = 'O'
            i -= direction[0] * item_count
            j -= direction[1] * item_count

        arr[position[0]][position[1]] = '.'
        arr[i][j] = '@'

        return i, j

if __name__ == '__main__':
    arr = []
    movement = []

    current_position = (0, 0)

    # read file
    with (open("real_map.in", 'r') as file):
        line_number = 0
        for line in file:
            arr.append(list(line[:-1]))
            if line.find('@') != -1:
                current_position = (line_number, line.index('@'))
            line_number += 1

    with (open("real_move.in", 'r') as file):
        for line in file:
            for char in line[:-1]:
               movement.append(char)
    print(movement)
    tct = 0

    for head in movement:
        match head:
            case '^':
                direction = (-1, 0)
            case '<':
                direction = (0, -1)
            case '>':
                direction = (0, 1)
            case 'v':
                direction = (1, 0)
            case _:
                print("unexpected direction")
                sys.exit()
        current_position = move(current_position, direction)

        '''
        print(tct)
        tct += 1
        for h in range(len(arr)):
            for w in range(len(arr[0])):
                print(arr[h][w], end='')
            print()
        '''
    gps = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'O':
                gps += i*100 + j

    print(gps)