import sys

if __name__ == '__main__':
    arr = []
    # well, I shouldn't do this
    sys.setrecursionlimit(3000)

    # read file
    with (open("real.in", 'r') as file):
        line_number = 0
        for line in file:
            arr.append(list(line[:-1]))
            if line.find('S') != -1:
                start = (line_number, line.index('S'))
                arr[start[0]][start[1]] = '.'
            line_number += 1

    best_score = 2147483647

    # key: (i, j), value: best score to this position
    visited = {(start[0], start[1]) : 0}

    def dfs(position, direction, score):
        global best_score, arr

        if score >= best_score:
            return

        i = position[0] + direction[0]
        j = position[1] + direction[1]

        if arr[i][j] == 'E':
            if score < best_score:
                best_score = score
            return

        if arr[i][j] == '#':
            return

        if arr[i][j] == '.':
            if (i, j) not in visited:
                visited[(i, j)] = score
            else:
                if visited[(i, j)] > score:
                    visited[(i, j)] = score
                else:
                    return

        if direction[0] == 0:
            dfs((i, j), direction, score+1)
            dfs((i, j), (-1, 0), score+1001)
            dfs((i, j), (1, 0), score+1001)
        elif direction[1] == 0:
            dfs((i, j), direction, score+1)
            dfs((i, j), (0, -1), score+1001)
            dfs((i, j), (0, 1), score+1001)

    dfs(start, (0, 1), 1)
    dfs(start, (-1, 0), 1001)
    dfs(start, (1, 0), 1001)
    print(best_score)