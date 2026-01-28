import math
def cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    
    volume = math.pi * (radius ** 2) * height
    return volume

try:
    print(cylinder_volume(3, 5))
except ValueError as e:
    print(e)