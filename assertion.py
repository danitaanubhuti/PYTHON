#function calling
def sum(a,b):
   return a+b
a=int(input("enter value of a "))
b=int(input("enetr value of b"))
print("you have entered {0} and {1}".format(a,b),end='')
result=sum(a,b)
print("  and the result is ",result)
#handle assetion satement
y=int(input("enter an intger"))
try:
  assert(y>0)
  print("entered input is ",y)
except AssertionError:
    print("wrong input")

