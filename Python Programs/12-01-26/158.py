#Write a python function to find k number of operations required to make all elements equal.

def min_operations_to_equal_elements(arr, k):
    if not arr:
        return 0

    target=arr[0]
    operations=0

    for num in arr:
        diff=abs(num-target)
        operations+=diff//k
        if diff % k != 0:
            operations+=1

    return operations



arr=[10, 20, 30]
k=5
print(min_operations_to_equal_elements(arr, k))  


