#operations on arrays
from array import*
#create an array with int values
arr = array('i', [10,20,30,40,50])
print('Original array:', arr)
#append 30 to the array arr
arr.append(30)
arr.append(60)
print('After appending 30 and 60:', arr)
#insert 99 at position number 1 in arr
arr.insert(1, 99)
print('After inserting 99 in 1st position:', arr)
#remove an element from arr
arr.remove(20)
print('After removing 20:', arr)
#remove last element using pop()method
n = arr.pop()
print('Array after using pop():', arr)
print('Popped element:', n)
#finding position of element using index() method
n = arr.index(30)
print('First occurrence of element 30 is at:', n)
#convert an array into a list using tolist() method
lst = arr.tolist()
print('List:', lst)
print('Array:', arr)

