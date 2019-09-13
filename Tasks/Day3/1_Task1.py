'''
num = int(input('enter one number: '))
if num % 2 == 0:
    print('number is an even number')
'''
'''
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if(a > b and a > c):
    print('First number is the largest number')
if(b > a and b > c):
    print('Second number is the largest number')
if(c > b and c > a):
    print('Third number is the largest number')
'''

a = 1
b = 2
c = False
condition = [a == 1, b == 2, c == True]

if all(condition):
    print('If all conditions are true')
if condition:
    print('Some conditions are true')


