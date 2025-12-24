def merge_three_dicts(d1, d2, d3):
    return {**d1,**d2,**d3}


a={'x':1,'y':2}
b={'y':3,'z':4}
c={'w':5}

merged=merge_three_dicts(a,b,c)
print(merged)
