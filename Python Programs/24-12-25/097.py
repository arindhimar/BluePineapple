from collections import Counter


def list_counter(tempLists):
    # tempList=[item for sublist in list_of_lists for item in sublist]
    tempList=[]
    for list in tempLists:
        tempList.extend(list)
    return Counter(tempList)



    