matrix = [[7,8,9],[1,2,3],[4,5,6]]

tempSum = {}

for i in range(len(matrix)):
    tempSum[i] = sum(matrix[i])

sortedDict = {key: value for key, value in sorted(tempSum.items(), key=lambda item: item[1],reverse=True)}

newMatrix = []

for i in sortedDict.keys():
    newMatrix.append(matrix[i])

print(newMatrix[0])
