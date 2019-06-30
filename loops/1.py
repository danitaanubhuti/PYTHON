#to dispaly charecters of a string
str="danita"
for x in str:
   print(x)
   
#to display charecters of a string using sequence index
str="danita"
n=len(str)
for i in range(n):
   print(str[i])
#to display even number using for loop
for i in range(1,10,2):
     print(i)
#to display numbers in decending order
for i in range(10,0,-1):
    print(i)
#to find sum of no in a list using for loop
lst={10,20,30,40}
sum=0
for i in lst:
    print(i)
    sum+=i
print('sum=',sum)
#using while loop
i=0
sum=0
lst=[10,20,30,40]
while i<len(lst):
    print(lst[i])
    sum+=lst[i]
    i+=1
print("sum=",sum)
