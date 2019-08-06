import sys
contents = sys.stdin.readlines()
arr = []
for i in contents:
    text = i.rstrip()
    text = text.rstrip("#")
    arr.append(text)
for x in arr:
    print(x)
