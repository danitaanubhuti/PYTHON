#unicode charecters
from array import *
#creating one array from another
a1=array('d',[1,2,0,3,4])
k=a1.typecode
a2=array(k,(a*45 for a in a1))
for i in a2:
   print(i)
