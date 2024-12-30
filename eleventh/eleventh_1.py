def blink(arr):
    new_arr = []
    for i in range(len(arr)):
        temp = arr[i]
        digit = 0
        while temp != 0:
            temp //= 10
            digit += 1

        if arr[i] == 0:
            new_arr.append(1)

        elif not (digit & 1):
            new_arr.append(arr[i] // (10 ** (digit >> 1)))
            new_arr.append(arr[i] % (10 ** (digit >> 1)))

        else:
            new_arr.append(arr[i] * 2024)

    return new_arr


if __name__ == '__main__':
    arr = []

    with (open('input.txt', 'r') as file):
        for line in file:
            arr = list(map(int, list(line.split(" "))))

    for blink_time in range(25):
        arr = blink(arr)

    print(len(arr))