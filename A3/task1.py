import sys
contents = int(sys.stdin.readline())
graphNum = 1

def toInt(arr):
    arr = list(map(int, arr))
    return arr

def traverse(graph):
    color = ["WHITE"]*len(graph)
    pred = [""]*len(graph)
    for s in graph:
        if color[s] == "WHITE":
            color[s] = "GREY"
            pred[s] = "null"
            while "GREY" in color:
                u = color.index("GREY")
                node = graph[u]
                if node == []:
                    pred[u] = "no neighbours"
                    color[u] = "BLUE" 
                for v in node:
                    if color[v] == "WHITE":
                        color[v] = "GREY"
                        pred[v] = u
                    else:
                        color[u] = "BLACK"
    return (pred)

while contents != 0:
    DicGraph = {x: toInt((sys.stdin.readline()).split()) for x in range(contents)}
    component = traverse(DicGraph)
    maxComponent = 0
    countComponent = 0
    for c in component:
        if c == "null":
            if countComponent > maxComponent:
                maxComponent = countComponent
            countComponent = 0
            countComponent += 1
        elif isinstance(c, int):
            countComponent += 1
    if countComponent > maxComponent:
        maxComponent = countComponent
    print("Graph "+str(graphNum)+" has a component of order "+str(maxComponent)+".")
    graphNum += 1
    contents = int(sys.stdin.readline())