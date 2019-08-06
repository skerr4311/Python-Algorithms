import sys
def main():
    #contents = ["blah#\n", "45 67#\n", "ddgfh fjhg gjkhgk#\n", "Input consists of many lines.#\n", "crean fresh#\n"]
    contents = sys.stdin.readlines()
    arr = []
    index = 0
    for i in contents:
        for x in i:
            if x == '#':
                text = i[:index]
                text = text.rstrip("#")
                arr.append(text)
                index = 0
            else:
                index = index + 1
    for x in arr:
        print(x)
if __name__=="__main__":
    main()