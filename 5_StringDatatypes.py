'''
a = "Double quote"
b = 'Single quote'
print(a, ' concat with ' ,b)
print(a+ ' concat with ' +b)
print(a,b)
'''

# str = 'programiz'
# print('str ', str)
# print('str[1] is', str[1])
# print('str[1:5] is', str[1:5])
# print('str[-1] is', str[-1])
# print('str[6:-1] is', str[6:-1])


# str2="HELLO WORLD"
# print(str2[2:7])
# print(str2[3:-2])

# str1 = 'Rekha'
# str2 = 'Python'
# print(str1,str2)
# print(str1*3)
# print(str2*3)

# user1 = input('Write something:')
# print(user1)
# user2 = input('Write something new:')
# print(user2)
# print(user1, user2)

'''
a,b = input("Enter 2 values: ").split()
print("Number of boys: ",a)
print("Number of girls: ",b)

x,y,z = input("Enter 3 values: ").split()
print("Number of boys: ",a)
print("Number of girls: ",b)
print("Number of teachers: ",b)
'''

a,b = input("Enter 2 values: ").split()
sum = int(a) + int(b)
dif = int(a) - int(b)
mul = int(a) * int(b)
div = int(a) / int(b)
# print("Sum of {0} and {1} is {2}".format(a,b,sum))
# print("Difference of {0} and {1} is {2}".format(a,b,dif))
# print("Multiplication of {0} and {1} is {2}".format(a,b,mul))
# print("Division of {0} and {1} is {2}".format(a,b,int(div)))

print(f"Sum of {a} and {b} is {sum}")
