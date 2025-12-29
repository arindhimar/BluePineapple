sortList=lambda s:sorted(s)

def sortSubLists(tempLists):
    return list(map(sortList,tempLists))



print(sortSubLists(["bac","cda","rdx"]))
        