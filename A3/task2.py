import sys
contents = int(sys.stdin.readline())

def toInt(arr):
    arr = list(map(int, arr))
    return arr

def adjacencyMatrix(graph):
    print(contents)
    for s in graph:
        matrix = [0]*contents
        stringMatrix = ""
        for x in graph[s]:
            matrix[x] = 1
        for m in matrix:
            stringMatrix = stringMatrix + str(m) + " "
        print(stringMatrix)


while contents != 0:
    DicGraph = {x: toInt((sys.stdin.readline()).split()) for x in range(contents)}
    adjacencyMatrix(DicGraph)
    contents = int(sys.stdin.readline())
print(contents)