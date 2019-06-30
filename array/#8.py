from numpy import *
#log space
n=logspace(1,4,5)
h=len(n)
for i in range(h):
   print("%.1f"%n[i],end='  ')
k=arange(1,5,2)
print(k)
#creating arrays using zeros() and ones()
from numpy import *
a = zeros(5, int)
print(a)
b = ones(5)
#default datatype is float
print(b)

