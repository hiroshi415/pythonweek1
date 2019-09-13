'''
score = 0
a = str(input('Is Python a interpreted language? (Yes, No): '))

if a == 'Yes':
    print('That is correct!')
    score += 1
else:
    print('That is wrong')

b = str(input('Is Django a framework for Python? (Yes, No): '))
if b == 'Yes':
    print('That is correct!')
    score += 1
else:
    print('That is incorrect')

c = str(input('Is (Pyson) spelled correctly? (Yes, No): '))
if c == 'Yes':
    print('That is incorrect')
else:
    print('That is correct!')
    score += 1

print('You have finished the test!')
print('Your final score is ', score)
'''
'''
print('Enter 0 to exit')
a = int(input('Enter any number: '))

if a != 0:
    print('You have entered', a, '!')

print('Enter 0 to exit')
b = int(input('Enter any number: '))

if b == 0:
    exit()
else:
    print('You have entered', b, '!')
'''
'''
a = int(input('Enter a number: '))
if a % 2 == 0:
    print('You have entered an even number')
else:
    print('You have entered a odd number')
'''
'''
print('Enter 0 to exit()')
userinput = str(input('Enter an alphabet: '))
if userinput != 0:
    if (userinput >= 'a' and userinput <= 'z') or (userinput >= 'A' and userinput <= 'Z'):
        print(userinput, 'is an alphabet')
'''
'''
print('Enter 0 to exit()')
userinput = str(input('Enter an alphabet: '))
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if userinput != 0:
    if userinput in vowels:
        print(userinput, 'is a vowel')
    else:
        print(userinput, 'is not a vowel')
'''
'''
print('Enter x to exit()')
num1 = str(input('Enter first number: '))
if num1 == 'x':
    exit()
else:
    num2 = str(input('Enter second number: '))
    x = num1
    num1 = num2
    num2 = x
    print('After swapping, this is the result')
    print('First Number:', num1)
    print('Second Number:', num2)
    # print('First Number:', num2)
    # print('Second Number:', num1)
'''
'''
print('Enter x to exit()')
num1 = str(input('Enter first number: '))
if num1 != 'x':
    print('Area of the square is', int(num1)**2)
'''
'''
print('Enter x to exit()')
string = str(input('Enter a string: '))
if string != 'x':
    print('You have entered', string)
'''
'''
print('Enter x to exit()')
string = str(input('Enter a string and I will find its length: '))
if string != 'x':
    print('Length of the word', string, 'is', len(string))
'''
'''
print('Enter x to exit()')
string1 = str(input('Enter a first string: '))
if string1 != 'x':
    string2 = str(input('Enter a second string: '))
    if (string1 == string2):
        print(string1, '==', string2)
    else:
        print(string1, '!=', string2)
'''
'''
print('Enter x to exit()')
string1 = str(input('Enter a first string: '))
if string1 != 'x':
    print('Original input: ',)
'''
'''
print('Enter x to exit()')
print('Enter any two numbers:')
num1 = str(input())
if num1 != 'x':
    num2 = int(input())
    operator = str(input('Enter any operator (+, -, /, *): '))
    if operator == '+':
        print(num1, '+', num2, '=', int(num1) + num2)
    elif operator == '-':
        print(num1, '-', num2, '=', int(num1) - num2)
    elif operator == '/':
        print(num1, '/', num2, '=', int(num1) / num2)
    else:
        print(num1, '*', num2, '=', int(num1) * num2)
'''
'''
print('Enter x to exit()')
print('Enter scores for 5 subjects:')
num1 = str(input())
if num1 != 'x':
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    mark = (int(num1)+num2+num3+num4+num5)/5
    if mark >= 85:
        print('Score:', int(mark))
        print('Score:', float(mark), '%')
        print('Congrats, you have scored A+')
    elif (mark >= 70 and mark < 85):
        print('Score:', int(mark))
        print('Score:', float(mark), '%')
        print('Congrats, you have scored A')
    elif (mark >= 50 and mark < 70):
        print('Score:', int(mark))
        print('Score:', float(mark), '%')
        print('Congrats, you have scored B')
    elif (mark >= 35 and mark < 50):
        print('Score:', int(mark))
        print('Score:', float(mark), '%')
        print('Congrats, you have scored C')
    else:
        print('Score:', int(mark))
        print('Score:', float(mark), '%')
        print('You have failed the class')
'''
print('Enter x to exit()')
print('Enter 2 values:')
num1 = str(input())
if num1 != 'x':
    num2 = int(input())
    if int(num1) == num2:
        print('They are both same values')
    elif (int(num1) > num2):
        print('Largest of the given number is', num1)
    else:
        print('Largest of the given number is', num2)
