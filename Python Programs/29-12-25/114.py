from collections import Counter

def append_freq(tempListOfTuples):
    tempCount=[]
    for i in tempListOfTuples:
        tempCount.append([i,Counter(i)])
    
    return tuple(tempCount)

print(append_freq(((1, 2, 3, 3), (4, 4, 2, 2))))
