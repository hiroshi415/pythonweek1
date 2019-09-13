'''user = int(input('enter a number: '))
fact = 1
for x in range(1, user+1):
    fact *= x

print(fact)
'''
'''
user = int(input('Enter a number: '))
for x in range(0, user):
    print(x)
'''
'''
list = [1, 4, 6, 3, 5, 1]
sum = 0
for x in list:
    sum += x
print(sum)
'''
'''
user = int(input('Enter a number: '))
for x in range(1, 11):
    print(user, '*', x, '=', user*x)
'''
'''
for x in range(1, 10):
    print(str(x)*x)
'''
'''
for x in range(0, 6):
    print('* '*x, 's')
    if(x == 5):
        for y in range(4, 0, -1):
            print('* '*y, 's')
'''
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for x in list:
    if x == 6 or x == 9 or x == 11:
        continue
    print(x)

'''
'''
reverse = str(input('Enter a string: '))
for x in range(len(reverse)-1, -1, -1):
    print(reverse[x], end="")
'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
strings = ['a', 'b', 'c', 'd', 'e']
for x in strings[1: 4]:
    print(x)
