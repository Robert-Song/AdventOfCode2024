import sys

if __name__ == '__main__':
    a = 25358015
    b = 0
    c = 0
    instruction = list(map(int, "2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0".split(",")))
    print(instruction)

    pointer = 0

    def combo(n):
        global a, b, c
        if 0 <= n < 4:
            return n
        if n == 4:
            return a
        if n == 5:
            return b
        if n == 6:
            return c
        if n == 7:
            print("nope")
            sys.exit()

    output = ""
    while pointer < len(instruction):
        opcode = instruction[pointer]
        operand = instruction[pointer+1]
        match opcode:
            case 0:
                a = a // (2 ** combo(operand))
            case 1:
                b = b ^ operand
            case 2:
                b = combo(operand) % 8
            case 3:
                if a != 0:
                    pointer = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                output += str(combo(operand) % 8)
            case 6:
                b = a // (2 ** combo(operand))
            case 7:
                c = a // (2 ** combo(operand))
        pointer += 2

    print(output)