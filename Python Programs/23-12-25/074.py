def follows_ptrn(seq, ptrn):
    if len(seq)!=len(ptrn):
        return False
    
    for i in range(len(seq)):
        if seq[i] != ptrn[i]:
            return False
    
    return True




tempList=[1,2,3,4]
tempPtrn=[1,2,3,4]

print(follows_ptrn(tempList,tempPtrn))