import re

if __name__ == '__main__':
    sum = 0
    with (open('input.txt', 'r') as file):
        # Read each line in the file
        for line in file:
            x = re.findall("mul\([0-9]+,[0-9]+\)", line)
            for i in x:
                temp = i[4:-1].split(",")
                sum += int(temp[0]) * int(temp[1])

    print(sum)