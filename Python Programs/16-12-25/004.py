import heapq

h=[] 

#by def min heap
heapq.heapify(h)

tempNumList=[-1,-3,-4,1,4,5]

for i in tempNumList:
    heapq.heappush(h,-i)
    
    

print("Maximum : ",-h[0])