import sys
def main():
    contents = input()
    arr = []
    start = 0
    index = 0
    for i in contents:
        if i == '#':
            text = contents[start:index]
            text = text.lstrip(' ')
            arr.append(text)
            start = index + 1
            index = index + 1
        else:
            index = index + 1
    for x in arr:
        print(x)
if __name__=="__main__":
    main()