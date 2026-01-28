def color_combinations(n):
    colors = ['Red', 'Green', 'Blue']
    if n <= 0:
        return []
    
    for i in range(n - 1):
        colors = [c + ' ' + color for c in colors for color in ['Red', 'Green', 'Blue']]
    return colors

print(color_combinations(2))