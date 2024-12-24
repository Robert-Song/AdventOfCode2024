from enum import Enum

from numpy.f2py.auxfuncs import throw_error


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
                arr[i][j] = 'X'
            count += 1

    count = 1
    direction = Direction.NORTH
    print(i, j)
    try:
        while True:
            print(i, j)
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
            if(i_next < 0 or i_next >= len(arr) or j_next < 0 or j_next >= len(arr[0])):
                raise IndexError
            if arr[i_next][j_next] == '.':
                count += 1
                arr[i_next][j_next] = 'X'
                i = i_next
                j = j_next
            elif arr[i_next][j_next] == 'X':
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
    except IndexError: print("reached end")
    except: print("what?")
    else: print("infinite loop?")

    for i in range(len(arr)):
        print(arr[i])

    print(count)

