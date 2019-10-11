import sys
from math import sin, cos, sqrt, atan2, radians

def Distance(lat1, lon1, lat2, lon2):
    R = 6371

    dlon = radians(abs(lon2)) - radians(abs(lon1))
    dlat = radians(abs(lat2)) - radians(abs(lat1))

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return(R*c)

cases = int(sys.stdin.readline()) #number of tests
case_index = 0
while case_index != cases:
    cities = int(sys.stdin.readline()) #number of cities
    cities_index = 0
    while cities_index != cities:
        city = sys.stdin.readline().split()
        print(city)
        #start loading up a storage system
        cities_index += 1
    gass = int(sys.stdin.readline())
    #send it off to shortest path algorithm
    case_index += 1

