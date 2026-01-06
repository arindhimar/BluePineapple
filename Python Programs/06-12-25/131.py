def reverse_vowels_of_given_string(s):
    vowels='aeiouAEIOU'
    s_list=list(s)
    left,right=0,len(s) - 1

    while left<right:
        if s_list[left] not in vowels:
            left+=1
        elif s_list[right] not in vowels:
            right-=1
        else:
            s_list[left],s_list[right]=s_list[right],s_list[left]
            left+=1
            right-=1

    return ''.join(s_list)


input_string=input("Enter a string: ")
result=reverse_vowels_of_given_string(input_string)
print(result)