if __name__ == '__main__':
    def checker(a_in):
        a = a_in
        b = 0
        c = 0
        instruction = list(map(int, "2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0".split(",")))

        pointer = 0

        output = ""
        while pointer < len(instruction):
            opcode = instruction[pointer]
            operand = instruction[pointer + 1]
            match opcode:
                case 0:
                    a = a // 8
                case 1:
                    b = b ^ operand
                case 2:
                    b = a % 8
                case 3:
                    if a != 0:
                        pointer = operand
                        continue
                case 4:
                    b = b ^ c
                case 5:
                    output += str(b % 8)
                case 6:
                    b = a // (2 ** b)
                case 7:
                    c = a // (2 ** b)
            pointer += 2

        return int(output)


    check = list(map(int, "2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0".split(",")))[::-1]
    print(check)
    result = 0
    target = ""
    for i in check:
        target = str(i) + target
        for j in range(8):
            if checker(result+j) == int(target):
                print(j)
        user = input("choose one: ")
        result += int(user)
        result *= 8

    print(result)
