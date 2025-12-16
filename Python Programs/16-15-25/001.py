def findMinCost(costMatrix,m,n):
    minCost=0
    minPath=[]
    
    calcMatrix=[]
    tempRow=[costMatrix[0][0]]
    
    for i in range(1,n):
        print(sum(tempRow)+costMatrix[0][i])
        tempRow.append(sum(tempRow)+costMatrix[0][i])
    calcMatrix.append(tempRow)
    for j in range(1,m):
        calcMatrix.append(sum())
    # print(tempRow)




costMatrix=[[1,2,6],[5,4,3],[9,7,8]]
m=int(input("Enter value for m "))
n=int(input("Enter value for n "))


print(findMinCost(costMatrix,m,n))