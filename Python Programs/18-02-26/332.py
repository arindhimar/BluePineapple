def count_frequency_char(str):
    count={}
    
    list_str = list(str)
    
    for i in list_str:
        if i != ' ':
            if i in count.keys():
                count[i]+=1
            else:
                count[i]=1

    return count


print(count_frequency_char("abcabcdfredf"))
    