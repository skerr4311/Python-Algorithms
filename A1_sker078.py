import sys
def main():
    contents = sys.stdin.readlines()
    arr = []
    for i in contents:
        text = i.rstrip("\n")
        text = text.rstrip("#")
        arr.append(text)
    for x in arr:
        print(x)
if __name__=="__main__":
    main()