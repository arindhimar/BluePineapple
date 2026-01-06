def find_divisors(n):
    divisors=[]
    for i in range(1, n + 1):
        if n%i==0:
            divisors.append(i)
    return divisors

def amicable_numbers(n):
    amicable_pairs=[]
    for num in range(2, n):
        sum_divisors=sum(find_divisors(num)) - num
        if sum_divisors!=num:
            sum_divisors_of_pair=sum(find_divisors(sum_divisors))-sum_divisors
            if sum_divisors_of_pair==num:
                pair=tuple(sorted((num, sum_divisors)))
                if pair not in amicable_pairs:
                    amicable_pairs.append(pair)
    return amicable_pairs


n=int(input("Enter a number: "))
pairs=amicable_numbers(n)
print(pairs)