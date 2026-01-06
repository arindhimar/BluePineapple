import cmath
import math


def find_angle(x, y):
    angle=cmath.phase(complex(x, y))
    return angle




imaginary_number=complex(3, 4)
angle=find_angle(imaginary_number.real, imaginary_number.imag)
print(angle)