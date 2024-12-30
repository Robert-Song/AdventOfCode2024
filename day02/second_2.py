def orderingDecision(a, b, c, d):
    bloomFilter = 0

    if b > a :
        bloomFilter = bloomFilter + 1
    if c > b :
        bloomFilter = bloomFilter + 1
    if d > c :
        bloomFilter = bloomFilter + 1

    if bloomFilter >= 2:
        return True

    return False


if __name__ == '__main__':
    with (open('input.txt', 'r') as file):
        # order 0 -> decreasing
        # order 1 -> increasing
        ordering: bool = False
        safeCount = 0
        warning = False

        debugline =0

        # Read each line in the file
        for line in file:
            debugline += 1

            warning = False
            # read each line

            temp = line.strip().split()
            temp = list(map(lambda x: int(x), temp))

            # with new implementation, if we have less than 3 input, then it will always be considered as safe
            if len(temp) <= 3:
                safeCount += 1
                continue

            ordering = orderingDecision(temp[0], temp[1], temp[2], temp[3])
            safeCount += 1

            i = 0
            while i < len(temp)-1:
                if (ordering and temp[i] >= temp[i+1]) or ((not ordering) and (temp[i] <= temp[i+1])) or (abs(temp[i] - temp[i+1]) > 3):
                    if warning:
                        safeCount -= 1
                        break
                    elif i == len(temp)-2:
                        break
                    elif (i == 0) and ((ordering and temp[i+1] < temp[i+2]) or ((not ordering) and temp[i+1] > temp[i+2])) and (
                                abs(temp[i+1] - temp[i+2]) <= 3):
                        warning = True
                        i = i+2
                        continue
                    elif (ordering and temp[i] >= temp[i+2]) or (((not ordering) and temp[i] <= temp[i+2])) or (abs(temp[i] - temp[i+2]) > 3):
                        safeCount -= 1
                        break
                    else:
                        warning = True
                        i = i + 2
                        continue
                i = i + 1

            print(debugline, temp, ordering, safeCount, warning, i)

        print(safeCount)