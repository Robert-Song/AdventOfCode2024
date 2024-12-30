from collections import deque
from queue import Queue


if __name__ == "__main__":
    #input edges
    edges = []
    #topologically sorted edges (kahn's algorithm - BFS)
    topoSorted = []

    #result input
    check = []

    #sum (result)
    sum = 0
    #check if this is an edge line or result line
    isResult = False

    #used to count how many nodes
    #use len(thisSet) to find number of nodes
    nodeList = set()

    #input file preprocessing
    with (open('input.txt', 'r') as file):
        for line in file:
            #edge lines
            if not isResult:
                #at this point, result line starts
                if line == "\n":
                    isResult = True
                    continue

                #make adjacency list from here
                temp = list(map(int, line[:-1].split('|')))
                nodeList.update(temp)
                edges.append(temp)

            #result lines
            if isResult:
                check.append(list(map(int, line[:-1].split(','))))

    revadj = [[] for _ in range(len(nodeList))]
    adj = [[] for _ in range(len(nodeList))]

    #k:node, v:position in array
    hashmap = {}
    i=0

    for node in nodeList:
        hashmap[node] = i
        i += 1

    # Constructing reverse adjacency list
    for edge in edges:
        revadj[hashmap[edge[1]]].append(edge[0])

    for edge in edges:
        adj[hashmap[edge[0]]].append(edge[1])

    '''
    print(nodeList)
    print(adj)
    print(check)
    '''

    # Performing topological sort
    print(revadj)
    print(adj)
    indegree = []
    # Vector to store indegree of each vertex
    for i in range(len(nodeList)):
        indegree.append(len(revadj[i]))

    print(indegree)
    # Queue to store vertices with indegree 0
    q = Queue(maxsize=0)
    for node in nodeList:
        if indegree[hashmap[node]] == 0:
            q.put(node)

    while not q.empty():
        # repeat for all possible cases
        node = q.get()
        topoSorted.append(node)

        for adjacent in adj[hashmap[node]]:
            indegree[hashmap[adjacent]] -= 1
        # If indegree becomes 0, push it to the queue
            if indegree[hashmap[adjacent]] == 0:
                q.put(adjacent)

    #print(nodeList)
    #print(topoSorted)




    correctTopo = True
    for i in check:
        correctTopo = True
        for j in range(len(i)-1, -1, -1):
            if not correctTopo : break
            for k in revadj[hashmap[i[j]]]:
                try:
                    value_index = i.index(k)
                except:
                    value_index = -1

                if value_index != -1 and value_index >= j:
                    correctTopo = False
                    break
        if correctTopo:
            sum += i[len(i)//2]
        '''
        if not correctTopo:
            count = 0
            targetIndex = len(i)//2
            for a in topoSorted:
                try:
                    value_index = i.index(a)
                except:
                    value_index = -1
                if value_index != -1 : count += 1
                if count == targetIndex+1:
                    sum += i[value_index]
                    break
        '''
    print(sum)
'''
    # Performing topological sort

    # Vector to store indegree of each vertex
    indegree = [0] * len(nodeList)

    for node in nodeList:
        for vertex in adj[hashmap[node]]:
            indegree[hashmap[vertex]] += 1

    print(indegree)

    # Queue to store vertices with indegree 0
    q = Queue(maxsize=0)
    for node in nodeList:
        if indegree[hashmap[node]] == 0:
            q.put(node)


    while not q.empty():
        #repeat for all possible cases
        i = q.qsize()
        thistopo = []
        for _ in range(i):
            node = q.get()
            thistopo.append(node)
            # Decrease indegree of adjacent vertices as the current node is in topological order
            for adjacent in adj[hashmap[node]]:
                indegree[hashmap[adjacent]] -= 1
                # If indegree becomes 0, push it to the queue
                if indegree[hashmap[adjacent]] == 0:
                    q.put(adjacent)

        topoSorted.append(thistopo.copy())
    print(topoSorted)
    if len(topoSorted) != len(nodeList):
        print("Graph contains cycle!")
    # Displaying result
    '''
'''
    print(thisSet)
    print(len(thisSet))
    print(edges)
    print(check)
'''


