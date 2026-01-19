import heapq 

def delete_smallest_and_insert(heap, item):
    heapq.heappushpop(heap, item)
    return heap

heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 11
print(delete_smallest_and_insert(heap, item))