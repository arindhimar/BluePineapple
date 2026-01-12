def sum_of_divisors(n):
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        return total

def are_sum_of_divisors_equal(num1, num2):
    return sum_of_divisors(num1) == sum_of_divisors(num2)

num1 = 6
num2 = 28
print(are_sum_of_divisors_equal(num1, num2))