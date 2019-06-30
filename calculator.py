#define all functions
def menu():
    print("welcome to calulator.py")
    print("your options are")
    print("1. Addition 2. Multiplication 3.Subtraction 4. Division")
    print("5.Quit")
    print("choose your option")
    input(option)
    return option

def add(a,b):
    print( a,"+",b,"=",a+b)
def sub(a,b):
    print (b,"-",a,"=",a-b)
def mul(a,b):
    print( a,"*",b,"=",a*b)
def div(a,b):
    print( a,"/",b,"=",a/b)
#NOW THE PROGRAM STARTS
loop=1
choice=0
while loop==1:
   choice=menu()
  if choice==1: 
     add(input("add this:"),input("to this:"));
  if choice==2:
      mul(input("multiply this:"),input("to this:"))
  if choice==3:
      sub(input("subtract this:"),input("to this:"))
  if choice==4:
      div(input("divid this:"),input("to this:"))
  elif:
      loop=0

  print("thank you for using calculator.py")
