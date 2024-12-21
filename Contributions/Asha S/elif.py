#1.WAP to check whether the user entered number is single digit or 2 digit or 3 digit or morethan that 
num=int(input('enter a number :'))
if num>0:
    number=str(num)
else:
    num=num*(-1)
    number=str(num)
if len(number)==1:
    print(f"{num} is a single digit")
elif len(number)==2:
    print(f"{num} is a two digit")
elif len(number)==3:
    print(f"{num} is a three digit")
else:
    print(f"{num} is morethan three digit")

#      (or)
# else:
#     num=num*(-1)
#     number=str(num)
#     if len(number)==1:
#         print(f"{num} is a single digit")
#     elif len(number)==2:
#         print(f"{num} is a two digit")
#     elif len(number)==3:
#         print(f"{num} is a three digit")
#     else:
#         print(f"{num} is morethan three digit")

############################################################

#2.wap to check greatest among 3 numbers entered by the user
num1=int(input('enter num1 :'))
num2=int(input('enter num2:'))
num3=int(input('enter num3 :'))
if num1>num2 and num1>num3:
    print(f"{num1} is greatest")
elif num2>num1 and num2>num3:
    print(f"{num2} is greatest")
elif num1==num2 and num1==num3:
    print('no greatest number')
else:
    print(f"{num3} is greatest")

############################################################

#3.wap to take marks from user and print grades accordingly
marks=int(input('enter the marks :'))
if 100>=marks>85:
    print('O')
elif 85>=marks>75:
    print('A+')
elif 75>=marks>65:
    print('A')
elif 65>=marks>50:
    print('B+')
else:
    print('pass')

############################################################

#4.wap to print the type of character entered by the user
char=input('enter the character :')
if 'A'<=char<='Z':
    print('uppercase')
elif 'a'<=char<='z':
    print('lowercase')
elif '0'<=char<='9':
    print('number')
else:
    print('special character')

############################################################

#5.wap to print type of two sets entered by the user
set1=eval(input('enter set1'))
set2=eval(input('enter set2'))
if set1<set2:
    print(f"{set1} is subset of {set2}")
elif set2<set1:
    print(f"{set2} is subset of {set1}")
elif set1==set2:
    print(f"{set1} is equal to {set2}")
else:
    print('no relation')

############################################################

#6.wap to print the relation b/w the two no entered by the user
num1=int(input('enter num1'))
num2=int(input('enter num2'))
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num2} is greater than {num1}")
else:
    print('they are equal')

############################################################

#7.wap to check type of the triangle 
side1=int(input('enter side1'))
side2=int(input('enter side2'))
side3=int(input('enter side3'))
if side1==side2 and side1==side3:
    print('equilateral')
elif side1==side2 or side1==side3 or side2==side3:
    print('isoscelus')
else:
    print('scalene')

############################################################

#8.wap to decide the bonus of an employee based on their experiance
experiance=int(input('enter your experiance'))
salary=int(input('enter your salary'))
if experiance>0 and experiance<=2:
    bonus=(salary*10)/100
    print(f"your bonus is {bonus}")
elif experiance>2 and experiance<=5:
    bonus=(salary*20)/100
    print(f"your bonus is {bonus}")
else:
    bonus=(salary*25)/100
    print(f"your bonus is {bonus}")