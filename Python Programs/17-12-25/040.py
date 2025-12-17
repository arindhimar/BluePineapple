from collections import Counter

def frequency_of_elements(list_of_lists):
    flat_list=[]
    for sublist in list_of_lists:
        flat_list.extend(sublist)
    return Counter(flat_list)

data=[[1,2,3],[2,3,4],[3,4,5]]

print(frequency_of_elements(data))