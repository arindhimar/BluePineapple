def check_validity(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

s=input("enter the string: ")
print(check_validity(s))