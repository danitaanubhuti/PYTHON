#mathematical operations on arrays
#import all from numpy module
from numpy import *
#create a numpy array using array() function
arr = array([10, 20, 30.5, -40])
print("Original array:", arr)
#do arithmetic operations on the elements of the array
print("After adding 5:", arr+5)
print("After subtracting 5:", arr-5)
print("After multiplying with 5:", arr*5)
print("After dividing with 5:", arr/5)
print("After modulus with 5:", arr%5)
#we can use the arrays in expressions also
print("Expression value:", (arr+5)**2-10)
print("Sin values:", sin(arr))
print("Cos values:", cos(arr))
print("Tan values:", tan(arr))
print("Biggest element:", max(arr))
print("Smallest element:", min(arr))
print("Sum of all elements:", sum(arr))
print("Average of all elements:", mean(arr))

