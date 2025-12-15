# a,b=5,7
a,b=4,6
xor=a^b
print(xor!=0 and (xor&(xor-1))==0)

