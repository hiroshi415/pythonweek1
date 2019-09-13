'''
# 1. swap 4 values of input
print('Enter x to exit()')
print('Enter 4 values:')
num1 = str(input())
if num1 != 'x':
    num2 = input()
    num3 = input()
    num4 = input()

    x = num1
    num1 = num4
    num4 = num3
    num3 = num2
    num2 = x
    print('If you sawp the numbers it is now')
    print('1:', num1)
    print('2:', num2)
    print('3:', num3)
    print('4:', num4)
'''
'''
# Calendar from userinput
import calendar

year = int(input('What year is it?: '))
m = int(input('What month is it?(in numbers): '))

print(calendar.month(year, m))
'''

'''
# 3. create simple calculator values from user input
print('1. Addition')
print('2. Substraction')
print('3. Division')
print('4. Multiplication')
print('5. Enter x to exit()')

choice = int(input())
if choice != 5:
    if choice == 1:
        print('Enter two values to add')
        num1 = int(input())
        num2 = int(input())
        print(num1, '+', num2, '=', num1+num2)
    if choice == 2:
        print('Enter two values to substract')
        num1 = int(input())
        num2 = int(input())
        print(num1, '-', num2, '=', num1-num2)
    if choice == 3:
        print('Enter two values to divide')
        num1 = int(input())
        num2 = int(input())
        print(num1, '/', num2, '=', num1/num2)
    if choice == 4:
        print('Enter two values to multiply')
        num1 = int(input())
        num2 = int(input())
        print(num1, '*', num2, '=', num1*num2)
'''
