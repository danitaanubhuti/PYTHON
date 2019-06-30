from numpy import *
a=array([10,20,30,40])
print("a=",a,end='  ')
b=array(a)
c=a
print("b=",b,end='  ')
print("c=",c)
m=linspace(0,100,4)
print(m)
k=array(['kjh','dhhnm','mhgh'],dtype=str)
print(k)
#log space
n=logspace(1,4,5)
h=len(n)
for i in range(h):
   print("%1f"%a[i],end='  ')
