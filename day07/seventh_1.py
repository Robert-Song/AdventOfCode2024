result_sum = 0

def recur_add(arr, n, target):
    #when we found the correct formula
    if n == 1:
        return True if arr[0] + arr[1] == target else False

    new_target = target - arr[n]

    #when this branch not worth traversing anymore
    if new_target < 0:
        return False

    if recur_mul(arr, n-1, new_target):
        return True
    if recur_add(arr, n-1, new_target):
        return True
    else:
        return False

def recur_mul(arr, n, target):
    # when we found the correct formula
    if n == 1:
        return True if arr[0] * arr[1] == target else False

    #when this branch not worth traversing anymore
    if target % arr[n] != 0:
        return False

    new_target = target / arr[n]

    if recur_mul(arr, n - 1, new_target):
        return True
    if recur_add(arr, n - 1, new_target):
        return True
    else:
        return False

if __name__ == '__main__':
    test_value = []
    numbers = []

    #input file preprocess
    with (open('input.txt', 'r') as file):
        for line in file:
            test_value.append(int(line[:line.index(':')]))
            numbers.append(list(map(int, line[line.index(':')+2:-1].split(' '))))

    for i in range(len(test_value)):
        if recur_add(numbers[i], len(numbers[i])-1, test_value[i]):
            result_sum += test_value[i]
        elif recur_mul(numbers[i], len(numbers[i])-1, test_value[i]):
            result_sum += test_value[i]
        else:
            continue

    print("sum: " + str(result_sum))
