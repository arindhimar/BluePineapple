import math
def highest_power_of_2(n):
    return 2**int(math.log2(n))

n=int(input("Enter n"))
print(highest_power_of_2(n))
