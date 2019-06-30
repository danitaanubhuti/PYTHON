#program to understand bytearray type array
#create a list of byte numbers
elements=[10,20,0,40,50]
x=bytearray(elements)
x[0]=88
x[1]=99
for i in x: print(i)
