import sys
from math import sin, cos, sqrt, atan2, radians

def Distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = abs(sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return(R*c)

def pathToStrng(graph, path):
    pred = len(path)-1
    answer = ""
    while pred != 0:
        city = graph[pred][2]
        pred = path[pred]
        answer = city + ", "+ answer
    answer = graph[0][2] + ", " + answer
    return(answer.rstrip(", "))

def Dijkstra(matrix, length, DicGraph):
    priorityQ = []
    path = [0]*length
    colour = ["WHITE"]*length
    dist = [0]*length
    colour[0] = "GREY"
    priorityQ.append([0,0])
    while priorityQ != []:
        priorityQ.sort(key = lambda x: x[1])
        t1 = priorityQ[0][1] #value to city
        u = priorityQ[0][0] #pointer to city
        priorityQ.pop(0)
        for x in range(0, length):
            t2 = t1 + matrix[u][x]
            if colour[x] == "WHITE":
                colour[x] = "GREY"
                path[x] = u
                priorityQ.append([x, t2])
            elif colour[x] == "GREY":
                for item in priorityQ: # need to make this more efficient "edit: added break"
                    if item[0] == x:
                        if item[1] > t2:
                            item[1] = t2
                            path[x] = u
                        break
        colour[u] = "BLACK"
        dist[u] = t1
    if dist[-1] == float('inf'):
        return("Not possible")
    else:
        return(pathToStrng(DicGraph, path))



def AdjacencyMatrix(length, gass, DicGraph):
    adjMatrix = []
    for m in range(0, length):
        adjMatrix.append([0]*length)
    # populate the matrix
    for y in range(0, length):
        lat1 = DicGraph[y][0]
        lng1 = DicGraph[y][1]
        for x in range(0, length):
            lat2 = DicGraph[x][0]
            lng2 = DicGraph[x][1]
            if adjMatrix[y][x] == 0:
                dist = (float(Distance(lat1, lng1, lat2, lng2)))
                if dist == 0 or dist > gass:
                    adjMatrix[y][x] = float('inf')
                    adjMatrix[x][y] = float('inf')
                else:
                    adjMatrix[y][x] = dist
                    adjMatrix[x][y] = dist
    return adjMatrix

def createDic():
    DicGraph = {}
    for x in range(cities):
        line = sys.stdin.readline().split()
        tempName = line[2:]
        name = ""
        for i in tempName:
            name = name + i + " "
        arr = [float(line[0]), float(line[1]), name.rstrip()]
        DicGraph.update({x: arr})
    return(DicGraph)

cases = int(sys.stdin.readline()) #number of tests
case_index = 0
while case_index != cases:
    cities = int(sys.stdin.readline()) #number of cities
    DicGraph = createDic()
    gass = float(sys.stdin.readline())
    adjMatrix = AdjacencyMatrix(cities, gass, DicGraph)
    distance = Dijkstra(adjMatrix, cities, DicGraph)
    print(distance)
    #send it off to shortest path algorithm
    case_index += 1

