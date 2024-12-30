from enum import Enum
import copy

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

if __name__ == '__main__':
    count = 0
    arr = []
    #read file, separate characters, save like a 2D array
    with (open('input.txt', 'r') as file):
        for line in file:
            arr.append(list(line[:-1]))
            if '^' in line:
                i = count
                j = line.index('^')
                arr[i][j] = "."
            count += 1

    count = 0
    direction = Direction.NORTH

    #outer loop for actual tracing
    while True:
        match direction:
            case Direction.NORTH:
                i_next = i - 1
                j_next = j
            case Direction.EAST:
                i_next = i
                j_next = j + 1
            case Direction.SOUTH:
                i_next = i + 1
                j_next = j
            case Direction.WEST:
                i_next = i
                j_next = j - 1
        #this is when we reach the end
        if i_next < 0 or i_next >= len(arr) or j_next < 0 or j_next >= len(arr[0]):
            break

        #place temp obstacle and check if we are stuck in the loop, if next path is empty path
        if arr[i_next][j_next] == '.' :
            #push settings that we need to use after checking the loop
            loopCheckDirection = direction
            loopChecki = i_next
            loopCheckj = j_next

            #copy the map to check
            loopCheckArr = copy.deepcopy(arr)
            #temp obstacle placed here
            loopCheckArr[i_next][j_next] = '#'

            while True:
                if loopCheckArr[i_next][j_next] == '.' or loopCheckArr[i_next][j_next] == 'O' or loopCheckArr[i_next][j_next] == 'X':
                    loopCheckArr[i_next][j_next] = ['+', direction]
                    i = i_next
                    j = j_next
                elif loopCheckArr[i_next][j_next] == '#':
                    match direction:
                        case Direction.NORTH:
                            direction = Direction.EAST
                        case Direction.EAST:
                            direction = Direction.SOUTH
                        case Direction.SOUTH:
                            direction = Direction.WEST
                        case Direction.WEST:
                            direction = Direction.NORTH
                elif loopCheckArr[i_next][j_next][0] == '+':
                    if direction in loopCheckArr[i_next][j_next]:
                        #loop found!
                        arr[loopChecki][loopCheckj] = 'O'
                        count += 1
                        break
                    else:
                        loopCheckArr[i_next][j_next].append(direction)
                        i = i_next
                        j = j_next

                #update next move
                match direction:
                    case Direction.NORTH:
                        i_next = i - 1
                        j_next = j
                    case Direction.EAST:
                        i_next = i
                        j_next = j + 1
                    case Direction.SOUTH:
                        i_next = i + 1
                        j_next = j
                    case Direction.WEST:
                        i_next = i
                        j_next = j - 1
                #this is when we don't have loop
                if i_next < 0 or i_next >= len(arr) or j_next < 0 or j_next >= len(arr[0]):
                    arr[loopChecki][loopCheckj] = 'X'
                    break
            #pop restore
            direction = loopCheckDirection
            i = loopChecki
            j = loopCheckj

        #this condition is already checked, so no need to double-check
        elif arr[i_next][j_next] == 'O' or arr[i_next][j_next] == 'X':
            i = i_next
            j = j_next
        elif arr[i_next][j_next] == '#':
            match direction:
                case Direction.NORTH:
                    direction = Direction.EAST
                case Direction.EAST:
                    direction = Direction.SOUTH
                case Direction.SOUTH:
                    direction = Direction.WEST
                case Direction.WEST:
                    direction = Direction.NORTH


    print(count)

