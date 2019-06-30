#nested loops
for i in range(4):
    for j in range(5):
         print("*","\n")

#to display stars in right angled triangular form
for i in range(1, 11): #to display 10 rows
    for j in range(1, i+1): #no. of stars = row number
        print('*', end='')
    print()


#right angle trinagle
for i in range(1,11):
       print('*'*(i))

#equilateral triangle
n=40
for i in range(1,11):
    print(''*n,end='')
    print('*'*(i))
    n=-1
