import sys
contents = int(sys.stdin.readline())
graphNum = 1

def toInt(arr):
    arr = list(map(int, arr))
    return arr

def BFS(i, graph):
    length = len(graph)
    color = ["WHITE"]*length
    pred = ["null"]*length
    d = ([""]*length)
    q = []
    for s in graph:
        if color[s] == "WHITE":
            #breadth-first search visit algorithm
            color[s] = "GREY"
            d[s] = 0
            q.append(s)
            node_counter = 1
            while q != []:
                u = q.pop(0)
                node = graph[u]
                for v in node:
                    if color[v] == "WHITE":
                        color[v] = "GREY"
                        pred[v] = u
                        d[v] = d[u]+1
                        q.append(v)
                        node_counter += 1
                color[u] = "BLACK"
            #end of breadth-first search visit algorithm
    return (d)

def diameterCheck(graph):
    diameterArr = []
    for s in graph:
        if graph[s] == []:
            return 0
    for i in range(0, contents):
        component = BFS(i, graph)
        diameterArr.append(max(component))
    return(diameterArr)

while contents != 0:
    DicGraph = {x: toInt((sys.stdin.readline()).split()) for x in range(contents)}
    component = diameterCheck(DicGraph)
    if component == 0:
        string = " is disconnected."
    else:
        string = " has diameter "+str(component)+"."
    print("Graph "+str(graphNum)+string)
    graphNum += 1
    contents = int(sys.stdin.readline())