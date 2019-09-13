# # 4 if else statment

# a = False
# b = 20
# c = 30
# d = 100

# if a:
#     print('only run if a is true')
#     if (d > b):
#         print('d is bigger than b')
#     else:
#         print('b is bigger than d')
#     if (c > b):
#         print('c is bigger than b')
#     else:
#         print('b is bigger than c')
#     if (b > d and b > c):
#         print('b is the biggest number')
#     else:
#         print('b is not the biggest number')
# else:
#     print('a is false')

'''
scoreA = 30
scoreB = 61

if (scoreA+scoreB <= 100):
    print('Score:', scoreA+scoreB, 'this is a valid test score')
else:
    print('Score:', scoreA+scoreB, 'test score should not exceed 100')
'''

maleAge = 16
femaleAge = 4


if(maleAge >= 18 and femaleAge >= 18):
    print('Both male and female can vote at their age')
    if(maleAge >= 21):
        print('The man can get married')
    else:
        print('The man cannot get married')

    if(femaleAge >= 18):
        print('The lady can get married')
    else:
        print('The lady cannot get married')

else:
    print('They cannot vote or get married')
