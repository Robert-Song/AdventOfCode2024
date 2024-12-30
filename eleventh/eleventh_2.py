from collections import Counter

def blink(input_stones):
    new_stones = Counter()

    for stone, number in input_stones.items():
        if stone == 0:
            new_stones[1] += number
        elif len(str(stone)) & 1 == 0:
            digit = len(str(stone)) >> 1
            new_stones[stone // (10 ** digit)] += number
            new_stones[stone % (10 ** digit)] += number
        else:
            new_stones[stone*2024] += number

    return new_stones



if __name__ == '__main__':
    arr = []

    with (open('input.txt', 'r') as file):
        for line in file:
            arr = list(map(int, list(line.split(" "))))

    stones = Counter(arr)
    print(stones)
    for blink_time in range(75):
        stones = blink(stones)
        print(stones)

    print(sum(stones.values()))