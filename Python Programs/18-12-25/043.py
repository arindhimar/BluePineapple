import re

pt=r'\b\w+_\w+\b'


print(re.findall(pt,"abc_def XYZ x_y test_case A_b c_d_e"))
