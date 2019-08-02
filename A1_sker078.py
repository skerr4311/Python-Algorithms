def main():
    f = open("text.txt", "r") #open a text file
    contents = f.readlines()
    arr = []
    i=1
    for x in contents:
        x = x.rstrip('\n')
        x = x.rstrip('#')
        arr.append(x)
    for z in arr:
        print(z)
        if i != len(arr):
            print('\n')
            i=i+1
if __name__=="__main__":
    main()