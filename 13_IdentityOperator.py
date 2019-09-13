'''
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3, 4, 5]
y3 = [1, 2, 3, 4, 5]
x = {1, 2, 3}
y = {1, 2, 3}

# Output false
print(x1 is not y1)

# Output true
print(x2 is y2)

# Output false
print(x3 is y3)
# Output is true
print(x3 == y3)

# Output false
print(x is y)
'''


today = "Saturday"
holiday = "Monday"
print('Today is holiday', today is holiday)
print('Today is not holiday', today is not holiday)
