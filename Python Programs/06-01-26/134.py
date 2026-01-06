def check_last_element_even_odd(arr, p):
    for i in range(p):
        arr =[x + 1 for x in arr]
    return "Even" if arr[-1]%2==0 else "Odd"

array=[1,2,3,4,5]
passes=3
print(check_last_element_even_odd(array, passes))