# # Matrix Adding
# a = [[2,3],
#     [4,5]]
# b = [[6,8],
#     [9,3]]


# x = [[12,7,3],
#     [4,5,6],
#     [7,8,9]]

# y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# ans = [[],[],[]]


# for i in range(0,len(x),1):
#     for j in range(0, len(y), 1):
#         ans[i].append(x[i][j] + y[i][j])
#     print(ans[i])


# # Transpose
# a = [12,7,4,5,3,8]
# ans = [[],[]]
# for i in range(0, len(a), 1):
#     if (i%2 == 0):
#         ans[0].append(a[i])
#     else:
#         ans[1].append(a[i])

# for j in range(0,len(ans),1):
#     print(ans[j])


# # GCD
# user1 = int(input('Enter first     value: '))
# user2 = int(input('Enter second value: '))

# divisible = []
# ans = 0

# for i in range (1, int(user1/2)+1, 1):
#     if(user1 % i == 0):
#         divisible.append(int(i))
# for j in range (0, len(divisible), 1):
#     if (user2 % divisible[j] == 0):
#         ans = divisible[j]

# print(ans)
'''
import math as m

x = 'rekha'
a = False


for i in range(0,m.floor(len(x)/2),1):
    if x[i] == x[-i-1]:
        a = True
    else:
        a = False

if a == True:
    print('This is a pelindrome')
else:
    print('This is not a pelindrome')'''

'''
print('Enter x to exit()')
number = str(input('Enter any number: '))

if number != 'x':
    if int(number) == 0:
        print('It is zero')
    elif int(number) > 0:
        print(number, 'is a positive number.')
    else:
        print(number, 'is a negative number.')
'''
'''
# day of the week

import datetime
year = int(input('Enter a year: '))
month = int(input('Enter a month(in numbers): '))
day = int(input('Enter a day: '))
slash = '/'

dayofweek = datetime.date(year, month, day).strftime("%A")
print(str(year)+slash+str(month)+slash+str(day), 'is', dayofweek)
'''

'''
# removing all bad characters
bad_chars = ('!"#$%&()=-~|^[]{}`@*:+;<>/_')

sentence = "T&HI(S) I!%S %!A) ME(S&)S{}Y S!EN#TNE}CE"
print("Original String : " + sentence)
for i in bad_chars:
    sentence = sentence.replace(i, '')

print("Organized string : " + str(sentence))
'''

'''
# sorting by alphabet
a = ("a", "h", "k", "e", "r", 'A', 'Z', 'K')
x = sorted(a)
print(x)
'''
'''
inputs = []
input1 = input("What is the input? ")
while input1 != "":
	inputs.append(input1)
	input1 = input("What is the input? ")

for i in range(len(inputs)):
    for j in range(0,len(inputs)-1, 1):
        if inputs[j] > inputs[j+1]:
            inputs[j], inputs[j+1] = inputs[j+1], inputs[j]

print(inputs)


a = str(input('Enter any strings: '))
b = ""
print(b.join(sorted(a)))
'''
