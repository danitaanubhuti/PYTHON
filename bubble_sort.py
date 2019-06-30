#sorting an array using Bubble sort technique
from array import*
#create an empty array to store integers

x = array('i', [])
#store elements into the array x
print('How many elements?', end='')
n = int(input()) #accept input into n

for i in range(n): #repeat for n times
   print('Enter element:', end='  ')
   x.append(int(input())) #add the element to the array x

print('Original array:', x)

#bubble sort
flag = False #when swapping is done, flag becomes True
for i in range(n-1): #i is from 0 to n-1
    for j in range(n-1-i): #j is from 0 to one element lesser than i
       if x[j] > x[j+1]: #if 1st element is bigger than the 2nd one
         t = x[j] #swap j and j+1 elements
         x[j] = x[j+1]
         x[j+1] =t
         flag = True  #swapping done, hence flag is True
    if flag==False: #no swapping means array is in sorted order
            break #come out of inner for loop
    else:
             flag = False #assign initial value to flag
print('Sorted array=', x)

