def find_focus(h, k, a, axis='x'):
    """
    axis = 'x'  → (y - k)^2 = 4a(x - h)
    axis = 'y'  → (x - h)^2 = 4a(y - k)
    """
    if axis == 'x':
        return (h + a, k)
    elif axis == 'y':
        return (h, k + a)
    else:
        raise ValueError("axis must be 'x' or 'y'")


print(find_focus(1, 2, 2, axis='x'))