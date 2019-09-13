'''
flag = True
if flag:
    print('This is a if statement')

if flag != True:
    print('only if flag is false')
'''
'''
num = 100
if num < 101:
    print('number is less than 100!')
'''
'''
scoreA = 59
scoreB = 49
if (scoreA + scoreB > 100):
    print('Total score is over 100')
'''
'''
list = ['hello', 'day', 'india']

if 'bangalore' in list:
    print('Bangalore is in the list')
if 'india' in list:
    print('India is in the list')
print('this is out of if statement')
'''
'''
list = ['hello', 'day', 'india']

if 'hello' in list:
    print('first statement passed')

    if 10<20:
        print('10<20 is true')
    print('default statement for second if')

    if 10 > 20:
        print('10>20 is not true')
    print('default statement for third if')
print('outside of if statement')
'''
'''
a = 1
b = 2
c = True

rules = [a == 11, b == 2, c == True]
if all(rules):
    print('All rules Success!')

if rules:
    print('one of the condition is true')
'''

a = 1
b = 2
c = 3
d = "hello"

if(a == 1 and b == 2 and c == 3 and d == "hello"):
    print('All conditions true')
