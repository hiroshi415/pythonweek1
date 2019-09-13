'''name = "Hiroshi"
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)'''


# fruits = ["apple", "peach", "mango"]
'''
for x in fruits:
    print(x)

for y in fruits:
    print(y)'''
'''
for z in fruits:
    if z == "peach":
        break
    print(z)

for x in fruits:
    if x == "peach":
        continue
    print(x)
'''

'''
for x in range(7):
    print(x+6)
for y in range(6, 13):
    print(y)
for z in range(0, 13, 3):
    print(z)
'''

'''
for x in range(6):
    print(x)
else:
    print('for loop is finished!')'''

adj = ["red", "big", "tasty"]
noun = ["apple", "peach", "mango"]
'''
for x in adj:
    print(x)
for y in noun:
    print(y)
'''
'''
# nested loop
for x in adj:
    for y in noun:
        print(x, y)
'''
'''
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
count_odd = 0
count_even = 0

for x in nums:
    if x % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print('Even numbers: ', count_even)
print('Odd numbers: ', count_odd)
'''
'''
datalist = [12, 12.312, 10j, False, 'hirosih',
            ('tuple', 12), [5, 10], {'a': 12, 'b': 73}]

for x in datalist:
    print('Type of', x, 'is', type(x))
'''
'''
dict = {'a': 1, 'b': 12, 'c': 13}
for x in dict:
    print(x)

for y in dict.values(): 
    print(y)
'''
'''
string = ["a", "b", "c", "d", "e"]
for x in string:
    print('String is', x)
'''