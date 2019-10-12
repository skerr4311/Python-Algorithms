import sys
from math import sin, cos, sqrt, atan2, radians

def Distance(lat1, lon1, lat2, lon2):
    R = 6371

    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)

    a = abs(sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return(R*c)


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
    adjMatrix = AdjacencyMatrix(cities, gass, DicGraph)
    for item in adjMatrix:
        print(item)
    #send it off to shortest path algorithm
    case_index += 1

