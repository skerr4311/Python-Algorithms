import sys
contents = sys.stdin.readlines()
arr = []
for i in contents:
    arr.append(i.rstrip())
for x in range(0, len(arr)):
    text = arr[x][0:-1]
    arr[x] = text
    print(arr[x])
sys.exit()