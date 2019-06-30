#input from other number systems
str = input('Enter hexadecimal number:')
#accept input as string
n = int(str, 16)
#inform the number is base 16
print('Hexadecimal to Decimal=', n);
str = input('Enter octal number:')
n = int(str, 8)
#inform the number is base 8
print('Octal to Decimal=', n);
str = input('Enter binary number:')
n = int(str, 2)
#inform the number is base 2
print('Binary to Decimal=', n);

