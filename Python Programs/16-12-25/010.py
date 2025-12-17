def nThSmallestItem(list1,n):
    if not list1:
        return "No dataset input"
    s=sorted(set(list1))
    if n<1 or n>len(s):
        return "n is out of range"
    return s[n-1]

list_of_numbers=[9,8,6,5,3,4,5,7,7,8,3,2]
print(nThSmallestItem(list_of_numbers,3))
