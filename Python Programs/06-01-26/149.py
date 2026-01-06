def find_longest_subsequence_with_adjacent_diff_one(arr):
    longest_subseq=[]
    current_subseq=[]

    for i in range(len(arr)):
        if i ==0 or abs(arr[i]-arr[i-1])==1:
            current_subseq.append(arr[i])
        else:
            if len(current_subseq)>len(longest_subseq):
                longest_subseq=current_subseq
            current_subseq=[arr[i]]

    if len(current_subseq)>len(longest_subseq):
        longest_subseq=current_subseq

    return longest_subseq


array=[4,5,6,3,2,3,4,5,6,7,8,1,2]
print(find_longest_subsequence_with_adjacent_diff_one(array))