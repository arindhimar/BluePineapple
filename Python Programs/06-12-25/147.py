def find_max_total_path_from_triagne(triangle):
    tempPath=[]
    tempSum=0
    
    for i in range(len(triangle)):
        max_ele = max(triangle[i])
        max_index=triangle[i].index(max_ele)
        
        tempSum+=max_ele
        tempPath.append(max_ele)
        

    return tempSum,tempPath


triangle=[
    [3],
    [7,4],
    [2,4,6],
    [8,5,9,3]
]

total,path=find_max_total_path_from_triagne(triangle)
print("Maximum total:",total)
print("Path:",path)
    