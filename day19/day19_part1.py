class Node:
    def __init__(self, data):
        self.data = data
        self.parent = 0
        self.children = []

if __name__ == '__main__':
    patterns = []
    count = 0
    file = "real.in"
    # read file, separate characters, save like a 2D array
    with (open(file, 'r') as file):
        patterns = file.readline()[:-1].split(", ")
        _ = file.readline()

        for line in file:
            root = Node(line[:-1])
            stack = [root]
            found = False
            while(stack):
                current = stack.pop()
                for pattern in patterns:
                    if current.data == pattern:
                        count += 1
                        found = True
                        break
                    if current.data.startswith(pattern):
                        newNode = Node(current.data[len(pattern):])
                        newNode.parent = current
                        current.children.append(newNode)

                if found:
                    break

                for child in current.children:
                    stack.append(child)

    print(count)
