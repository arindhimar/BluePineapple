def max_diff_binary_string(s):
    max_diff=0
    n=len(s)
    
    for i in range(n):
        count_0=0
        count_1=0
        for j in range(i, n):
            if s[j]== '0':
                count_0+=1
            else:
                count_1 +=1
            current_diff=count_0-count_1
            if current_diff >max_diff:
                max_diff=current_diff
    return max_diff


s=input("Enter a binary string: ")
result=max_diff_binary_string(s)

print(result)