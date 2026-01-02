def checkAllDictAreEmpty(ListOfDict):
    for i in ListOfDict:
        if len(i)!=0:
            return False
    
    return True


# inp=[{},{},{"a":"a"}]

inp=[{},{}]


print(checkAllDictAreEmpty(inp))


