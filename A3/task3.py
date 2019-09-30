import sys
import math
contents = int(sys.stdin.readline())
graphNum = 1

def toInt(arr):
    arr = list(map(int, arr))
    return arr

def BFS(graph):
    length = len(graph)
    diameterArr = []
    for s in graph:
        pred = ["null"]*length
        d = [float("inf")]*length
        q = []
        color = ["WHITE"]*length
        if color[s] == "WHITE":
            #breadth-first search visit algorithm
            color[s] = "GREY"
            d[s] = 0
            q.append(s)
            while q != []:
                u = q.pop(0)
                node = graph[u]
                for v in node:
                    if color[v] == "WHITE":
                        color[v] = "GREY"
                        pred[v] = u
                        d[v] = d[u]+1
                        q.append(v)
                color[u] = "BLACK"
            #end of breadth-first search visit algorithm
        check = max(d)
        if check == float("inf"):
            return 0
        else:
            diameterArr.append(check)
        #print(d, check)
    return (max(diameterArr))

while contents != 0:
    DicGraph = {x: toInt((sys.stdin.readline()).split()) for x in range(contents)}
    component = BFS(DicGraph)
    if component == 0:
        string = " is disconnected."
    else:
        string = " has diameter "+str(component)+"."
    print("Graph "+str(graphNum)+string)
    graphNum += 1
    contents = int(sys.stdin.readline())