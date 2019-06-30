from array import *
#accept marks as a string
str = input('Enter marks: ').split(' ')
#store the marks into 'marks'array
marks = [int(num) for num in str]
#display the marks and find total
sum=0
for x in marks:
    print(x)
    sum=sum+x
print('Total marks:', sum)
#display percentage
n = len(marks)
#n = no. of elements in marks array
percent = sum/n
print('Percentage:', percent)
 
