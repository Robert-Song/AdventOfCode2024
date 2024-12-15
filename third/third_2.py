import re

if __name__ == '__main__':
    sum = 0
    output = open("output.txt", "w")

    with (open('input.txt', 'r') as file):
        # Read each line in the file
        fileString = ""
        for line in file:
            fileString += line

        preprocessedString = ""

        while(fileString.find("don't()") != -1):
            preprocessedString += fileString[:fileString.find("don't()")]
            fileString = fileString[fileString.find("don't()")+7:]
            fileString = fileString[fileString.find("do()")+4:]

        preprocessedString+=fileString

        output.write(preprocessedString)

        #xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
        #xmul(2,4)&mul[3,7]!^?mul(8,5))

        x = re.findall("mul\([0-9]+,[0-9]+\)", preprocessedString)

        for i in x:
            temp = i[4:-1].split(",")
            sum += int(temp[0]) * int(temp[1])

    print(sum)