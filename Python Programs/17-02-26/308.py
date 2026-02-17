def largest_products(list1, list2, k):
    products = []
    
    for a in list1:
        for b in list2:
            products.append(a * b)
    products.sort(reverse=True)
    return products[:k]


l1 = [1, 4, 2]
l2 = [3, 5]
k = 3

print(largest_products(l1, l2, k))
