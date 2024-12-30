if __name__ == '__main__':
    with (open('input.txt', 'r') as file):
        # order 0 -> decreasing
        # order 1 -> increasing
        ordering: bool = False
        safeCount = 0

        # Read each line in the file
        for line in file:
            # Print each line
            temp = line.strip().split()
            temp = list(map(lambda x: int(x), temp))

            if (temp[1] - temp[0] >= 0):
                ordering = True
            else:
                ordering = False

            safeCount += 1

            for value in range(len(temp)-1):
                if (ordering and temp[value] >= temp[value + 1]) or (((not ordering) and temp[value] <= temp[value + 1])) or (abs(temp[value] - temp[value+1]) > 3):
                    safeCount -= 1
                    break

        print(safeCount)