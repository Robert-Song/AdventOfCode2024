def recur_add(arr, n, currentValue, targetValue):
    currentValue = currentValue + arr[n]
    if n == len(arr)-1:
        if currentValue == targetValue:
            return True
        else:
            return False

    if recur_add(arr, n+1, currentValue, targetValue) : return True
    if recur_mul(arr, n+1, currentValue, targetValue) : return True
    if recur_concat(arr, n+1, currentValue, targetValue) : return True
    return False

def recur_mul(arr, n, currentValue, targetValue):
    currentValue = currentValue * arr[n]
    if n == len(arr) - 1:
        if currentValue == targetValue:
            return True
        else:
            return False

    if recur_add(arr, n + 1, currentValue, targetValue): return True
    if recur_mul(arr, n + 1, currentValue, targetValue): return True
    if recur_concat(arr, n + 1, currentValue, targetValue): return True
    return False

def recur_concat(arr, n, currentValue, targetValue):
    temp = arr[n]
    digit = 0
    while temp != 0:
        digit = digit + 1
        temp = temp // 10

    currentValue = currentValue * (10 ** digit)
    currentValue = currentValue + arr[n]

    if n == len(arr) - 1:
        if currentValue == targetValue:
            return True
        else:
            return False

    if recur_add(arr, n + 1, currentValue, targetValue): return True
    if recur_mul(arr, n + 1, currentValue, targetValue): return True
    if recur_concat(arr, n + 1, currentValue, targetValue): return True
    return False

if __name__ == '__main__':
    result_sum = 0
    numbers = []
    test_value = []
    #input file preprocess
    with (open('input.txt', 'r') as file):
        for line in file:
            test_value.append(int(line[:line.index(':')]))
            numbers.append(list(map(int, line[line.index(':')+2:-1].split(' '))))

    print(numbers)

    for i in range(len(test_value)):
        if recur_add(numbers[i], 1, numbers[i][0], test_value[i]):
            result_sum += test_value[i]
        elif recur_mul(numbers[i], 1, numbers[i][0], test_value[i]):
            result_sum += test_value[i]
        elif recur_concat(numbers[i], 1, numbers[i][0], test_value[i]):
            result_sum += test_value[i]


    print("sum: " + str(result_sum))
