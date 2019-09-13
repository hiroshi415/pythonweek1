# course = "science"
# scoreA = 50
# scoreB = 40
'''
if(scoreA > 50):
    print('Score cannot exceed 50')
elif(scoreB > 50):
    print('Score cannot exceed 50')
else:
    print('Score validated, the total is ', scoreA+scoreB)
'''
'''
if(scoreA > 50):
    print('Score cannot exceed 50')
else:
    if(scoreB > 50):
        print('Score cannot exceed 50')
    else:
        print('Score validated, the total is ', scoreA+scoreB)
'''
'''
if(course.lower() == "science"):
    if(scoreA > 50):
        print('Score cannot exceed 50')
    elif(scoreB > 50):
        print('Score cannot exceed 50')
    else:
        print('Score validated, the total for', course, ' is ', scoreA+scoreB)
elif(course.lower() == "english"):
    if(scoreA > 60):
        print('Score cannot exceed 50')
    elif(scoreB > 40):
        print('Score cannot exceed 50')
    else:
        print('Score validated, the total for', course, ' is ', scoreA+scoreB)
else:
    print('Please check your course')
'''
'''
mark = int(input('Enter your score: '))
if mark >= 85:
    print('Congrats, you have scored A+')
elif (mark >= 70 and mark < 85):
    print('Congrats, you have scored A')
elif (mark >= 50 and mark < 70):
    print('Congrats, you have scored B')
elif (mark >= 35 and mark < 50):
    print('Congrats, you have scored C')
else:
    print('You have failed the class')
'''
'''
val = int(input('Enter a value: '))
if(val == 10 or val == 50 or val == 100):
    if(val == 10):
        print('Your value matches 10!')
    elif(val == 50):
        print('Your value matches 50!')
    else:
        print('Your value matches 100!')
else:
    print('You value has no match')
'''

question = str(input('Which Python data type is an ordered sequence? '))
if (question.lower() == 'tuple' or question.lower() == 'list'):
    print('You have entered:', question.lower())
    print('Your answer is correct')
else:
    print('You have entered:', question.lower())
    print('Your answer is incorrect')


