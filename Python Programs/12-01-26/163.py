import math
def polygon_area(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

n = 5
s = 6
print(polygon_area(n, s))