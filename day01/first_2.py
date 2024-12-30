if __name__ == '__main__':

    leftArray = []

    # k : number, v = occurrence
    rightHashMap = {}

    with open('input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            temp = line.strip().split()
            leftArray.append(int(temp[0]))

            if int(temp[1]) not in rightHashMap:
                rightHashMap[int(temp[1])] = 0

            rightHashMap[int(temp[1])] = rightHashMap[int(temp[1])]+1

    sum = 0

    for i in range(len(leftArray)):
        if leftArray[i] not in rightHashMap:
            continue
        sum += leftArray[i] * int(rightHashMap.get(leftArray[i]))

    print(sum)



