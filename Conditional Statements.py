# In Python IF is the only conditional statement
# The below are the IF ELSE STATEMENTS
# balance = 100
# withdraw = 20
# if withdraw <= balance:
#     print('withdraw success' )
# else:
#     print('Insufficient Funds')
#
#
# balance = 100
# withdraw = 200
# if withdraw <= balance:
#     print('withdraw success' )
# else:
#     print('Insufficient Funds')
#
# balance = 100
# withdraw = 20
# name = 'Howard'
# if withdraw <= balance and name == 'Said':
#     print('withdraw success')
# else:
#     print('Insufficient Funds or Not Said')
#
#
#
#
#
#
#
# # The below are if-elif -else statements
# score = ''
#
# if score == 'Excellent':
#     print('Green Label')
# elif score == 'Good':
#     print('Blue Label')
# elif score == 'Poor':
#     print('Red Label')
# else:
#     print('Unrecognized')
#
# score = 'Excellent'
# if score == 'Excellent':
#     print('Green Label')
# elif score == 'Good':
#     print('Blue Label')
# elif score == 'Poor':
#     print('Red Label')
# else:
#     print('Unrecognized')
#

# Grade students based on
# ask a user to enter the following marks
# math - Use input function
# kis
# ssr
# sci
# calculate
# total
# average
# using average give grade to student (use an if - elif statement)
# 80 - 100 = 'A'
# 70 - <79 = 'B'
# 60 - <70 = 'C'
# 50 - <60 = 'D'
# <50 = 'E'

math = input('enter math score')
print(math)

Kis = input('enter Kiswahili score')
print(Kis)

Ssr = input('enter Ssr score')
print(Ssr)

Sci = input('enter Sci score')
print(Sci)

math1 = int(math)
Kis1 = int(Kis)
Ssr1 = int(Ssr)
Sci1 = int(Sci)

total = math1 + Kis1 + Ssr1 + Sci1
print(total)

actualtotal = int(total)
print(actualtotal)

average = actualtotal/4
print(average)

if average >= 80 and average <= 100 :
    print('A - Distinction')
elif average >= 70 and average < 80:
    print('B - Good')
elif average >= 60 and average < 70:
    print('C - Pass')
elif average >= 50 and average < 60:
    print('D - Fail')
elif average < 50:
    print('E - Super Fail')

else:
    print('Exam not done - Kuja na Mzazi')


