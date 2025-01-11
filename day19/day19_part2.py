if __name__ == '__main__':
    possible = {}
    patterns = []
    result = 0


    def possible_cases(design):
        if len(design) == 1:
            return 1

        if design in possible:
            return possible[design]

        count = 0
        for pattern in patterns:
            if design.startswith(pattern):
                count += possible_cases(design[len(pattern):])

        possible[design] = count
        return count


    file = "real.in"
    with (open(file, 'r') as file):
        patterns = file.readline()[:-1].split(", ")
        _ = file.readline()

        for line in file:
            result += possible_cases(line)

    print(result)
