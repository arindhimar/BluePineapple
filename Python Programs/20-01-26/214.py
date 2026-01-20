import math
def convert_randians_to_degrees(randians):
    degrees = randians * (180.0 /math.pi)
    return degrees

randians = 3.0
print(convert_randians_to_degrees(randians))