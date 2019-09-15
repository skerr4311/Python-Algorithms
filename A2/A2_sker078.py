import sys
contents = sys.stdin.readlines()
pointer = 0
contents_length = (len(contents)) - 1

def shellSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    gap = length // 2
    while gap > 0:
        for start in range(gap):
            gapSort(arr, start, gap)
        gap = gap // 2

def gapSort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        currVal = arr[i]
        position = i
        while position >= gap and arr[position-gap]<currVal:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position]=currVal

#seperating out the read list
while pointer <= len(contents)-1:
    tempArr = []
    if contents[pointer][0].isdigit():
        tempArr = [int(x) for x in contents[pointer].split()]
    else:
        tempArr = contents[pointer].split()
    pointer += 1
    shellSort(tempArr)
    text = ""
    for item in range(0, len(tempArr)):
        text = text + str(tempArr[item]) + " "
    print(text)
sys.exit()