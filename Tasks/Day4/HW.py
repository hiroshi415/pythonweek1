# Sum of all the digits
number = str(input('Enter a number: '))
a = 0
b = 0
while b < len(number):
    a += int(number[b])
    b += 1
print('Sum of the digits are:', a)

# Armstrong numbers
armnum = str(
    input('Enter one armstrong number, (0, 1, 153, 370, 371, 407...):'))
c = 0
d = 0
while d < len(armnum):
    c += int(armnum[d])**int(len(armnum))
    print('Number', d+1, ':', int(armnum[d]), '^',
          int(len(armnum)), '=', int(armnum[d])**int(len(armnum)))
    d += 1
print(c)

