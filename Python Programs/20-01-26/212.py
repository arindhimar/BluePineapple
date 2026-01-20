
def sum_of_fourth_power(n):
    return sum(i**4 for i in range(1, n+1))

n = 5
result = sum_of_fourth_power(n)
print(result)
