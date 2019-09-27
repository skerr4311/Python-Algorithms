import sys
contents = int(sys.stdin.readline())
graphNum = 1

def toInt(arr):
    arr = list(map(int, arr))
    return arr

def BFS(graph):
    length = len(graph)
    color = ["WHITE"]*length
    pred = ["null"]*length
    d = [""]*length
    q = []
    maxNode_counter = 0
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
            if node_counter > maxNode_counter:
                maxNode_counter = node_counter
            #end of breadth-first search visit algorithm
    return (maxNode_counter)

while contents != 0:
    DicGraph = {x: toInt((sys.stdin.readline()).split()) for x in range(contents)}
    component = BFS(DicGraph)
    print("Graph "+str(graphNum)+" has a component of order "+str(component)+".")
    graphNum += 1
    contents = int(sys.stdin.readline())