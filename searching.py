#Searching an array for an element.
from array import*
#create an empty array to store integers
x = array('i', [])
#store elements into the array x
print('How many elements?', end='')
n = int(input())
#accept input into n
for i in range(n): #repeat for n times
    print('Enter element:', end='')
    x.append(int(input())) #add the element to the array x
print('Original array:', x)
print('Enter element to search:', end='')
s = int(input()) #accept element to be searched
#linear search or sequential search
flag=False #this becomes True if element is found
for i in range(len(x)): #repeat i from 0 to no. of elements
    if s == x[i]:
        print('Found at Position=', i+1)
        flag=True
if flag==False:
        print('Not found in the array')

#index() method gives the location of the element in the array
try:
    pos = x.index(s)
    print('Found at Position=', pos+1)
except ValueError:
#if element not found then ValueError will rise
    print('Not found in the array')

