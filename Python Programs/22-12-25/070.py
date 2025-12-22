def find_if_eqal_length(tempTuples):
    l=len(tempTuples)
    for i in range(1,l):
        if len(tempTuples[i])!=len(tempTuples[i-1]):
            print("Not equal")
            break
        
    print("Equal")