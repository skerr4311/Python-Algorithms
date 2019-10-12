import sys
from math import sin, cos, sqrt, atan2, radians

def Distance(lat1, lon1, lat2, lon2):
    R = 6371

    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)

    a = abs(sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return(R*c)

def Dijkstra(matrix, length):
    priorityQ = []
    path = []
    for m in range(0, length):
        path.append([0])
    colour = ["WHITE"]*length
    dist = [0]*length
    colour[0] = "GREY"
    priorityQ.append([0,0])
    while priorityQ != []:
        priorityQ.sort(key = lambda x: x[1])
        #print(priorityQ)
        t1 = priorityQ[0][1] #value to city
        u = priorityQ[0][0] #pointer to city
        priorityQ.pop(0)
        for x in range(0, length):
            t2 = t1 + matrix[u][x]
            if colour[x] == "WHITE":
                colour[x] = "GREY"
                priorityQ.append([x, t2])
            elif colour[x] == "GREY":
                for item in priorityQ: # need to make this more efficient
                    if item[0] == x:
                        if item[1] > t2:
                            item[1] = t2
        colour[u] = "BLACK"
        dist[u] = t1
        print(dist)
    return(dist)



def AdjacencyMatrix(length, gass, DicGraph):
    adjMatrix = []
    for m in range(0, length):
        adjMatrix.append([0]*length)
    # populate the matrix
    for y in range(0, length):
        lat1 = float(DicGraph[y][0])
        lng1 = float(DicGraph[y][1])
        for x in range(0, length):
            lat2 = float(DicGraph[x][0])
            lng2 = float(DicGraph[x][1])
            if adjMatrix[y][x] == 0:
                dist = (int(Distance(lat1, lng1, lat2, lng2)))
                if dist == 0 or dist > gass:
                    adjMatrix[y][x] = float('inf')
                    adjMatrix[x][y] = float('inf')
                else:
                    adjMatrix[y][x] = dist
                    adjMatrix[x][y] = dist
    return adjMatrix

cases = int(sys.stdin.readline()) #number of tests
case_index = 0
while case_index != cases:
    cities = int(sys.stdin.readline()) #number of cities
    DicGraph = {x: sys.stdin.readline().split() for x in range(cities)}
    gass = int(sys.stdin.readline())
    #adjMatrix = AdjacencyMatrix(cities, gass, DicGraph)
    test = [[float('inf'), 4, 1, float('inf'), float('inf')],
    [4, float('inf'), 5, 2, float('inf')],
    [1, 5, float('inf'), 2, 2],
    [float('inf'), 2, 2, float('inf'), float('inf')],
    [float('inf'), float('inf'), 2, float('inf'), float('inf')]]
    #distance = Dijkstra(adjMatrix, cities)
    distance = Dijkstra(test, 5)
    if distance[-1] == float('inf'):
        print("Not possible")
    else:
        print(distance)
    #send it off to shortest path algorithm
    case_index += 1

