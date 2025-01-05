import sys


# left and right case
def lr_move(position, direction):
    i = position[0]
    j = position[1] + direction[1]
    item_count = 0

    while arr[i][j] == '[' or arr[i][j] == ']':
        item_count += 1
        j = j + direction[1]

    if arr[i][j] == '#':
        return position

    if arr[i][j] == '.':
        while item_count >= 0:
            arr[i][j] = arr[i][j-direction[1]]
            j -= direction[1]
            item_count -= 1
        arr[i][j] = '.'
        return i, j+direction[1]

# up and down case
def ud_move(position, direction):
    i = position[0] + direction[0]
    j = position[1]

    if arr[i][j] == '#':
        return position

    if arr[i][j] == '.':
        arr[i][j] = '@'
        arr[position[0]][position[1]] = '.'
        return (i, j)

    item_count = 0
    affected_items = []
    if arr[i][j] == '[' or arr[i][j] == ']':
        affected_items.append([])
        if arr[i][j] == '[': affected_items[item_count] += (i, j), (i, j+1)
        if arr[i][j] == ']': affected_items[item_count] += (i, j-1), (i, j)
        item_count += 1

        while True:
            affected_items.append([])
            for i, j in affected_items[item_count-1]:
                if arr[i+direction[0]][j] == '#':
                    return position
                if arr[i+direction[0]][j] == '[':
                    if (i+direction[0], j) not in affected_items[item_count]:
                        affected_items[item_count].append((i+direction[0], j))
                        affected_items[item_count].append((i+direction[0], j+1))
                if arr[i+direction[0]][j] == ']':
                    if (i+direction[0], j) not in affected_items[item_count]:
                        affected_items[item_count].append((i + direction[0], j-1))
                        affected_items[item_count].append((i + direction[0], j))

            if affected_items[item_count] == []:
                for level in affected_items[::-1]:
                    #level = list(set(level))
                    for i, j in level:
                        arr[i+direction[0]][j] = arr[i][j]
                        arr[i][j] = '.'

                arr[position[0] + direction[0]][position[1]] = '@'
                arr[position[0]][position[1]] = '.'
                return position[0] + direction[0], position[1]

            item_count += 1




if __name__ == '__main__':
    arr = []
    movement = []

    current_position = (0, 0)

    # read file
    with (open("real_map.in", 'r') as file):
        line_number = 0
        for line in file:
            temp = []
            for char in line[:-1]:
                if char == '#': temp += '#', '#'
                elif char == 'O': temp += '[', ']'
                elif char == '.': temp += '.', '.'
                elif char == '@':
                    temp += '@', '.'
                    current_position = (line_number, line.index('@')*2)
            arr.append(temp)
            line_number += 1


    with (open("real_move.in", 'r') as file):
        for line in file:
            for char in line[:-1]:
               movement.append(char)

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
        if head == '>' or head == '<': current_position = lr_move(current_position, direction)
        elif head == '^' or head == 'v': current_position = ud_move(current_position, direction)

        '''
        print(tct)
        tct += 1
        for h in range(len(arr)):
            for w in range(len(arr[0])):
                print(arr[h][w], end='')
            print()
        '''

    for h in range(len(arr)):
        for w in range(len(arr[0])):
            print(arr[h][w], end='')
        print()

    gps = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '[':
                gps += i*100 + j

    print(gps)