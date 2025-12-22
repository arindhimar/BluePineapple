def maxDiffBwTuples(tempList):
    maxDiff=0
    for i in tempList:
        maxDiff=max(abs(i[0]-i[1]),maxDiff)
        
    print(maxDiff)


tempList=((17, 83), (4, 61), (92, 15), (38, 7), (56, 21))

maxDiffBwTuples(tempList)