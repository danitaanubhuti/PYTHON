#to search an element in a group of elemnts
grp=[10,20,30,40]
s=int(input("enter elent to search"))
for i in grp:
      if s==i:
         print("element found")
         break
else:
      print("element not found")
      
#to display numbers
x=10
for i in range(10,0,-1):
    if(i<6):
      pass
    else:
        print(i)

    
#using while loop
x=10
while(x>=1):
       print(x)
       x-=1
       if x==5:
         break
    
#to display numbers using continue
x=0
while x<10:
   x+=1
   if x>5:
       continue
   print("x=",x)

