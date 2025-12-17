def check(l1, l2):
    if all(item in l1 for item in l2):
        print("Yes")
    else:
        print("No")


l1 = (1, 2, 3, 4, 5, 6)
l2 = [3, 4, 2]

check(l1, l2)
