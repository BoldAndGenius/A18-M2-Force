# Q81.Write a program to check weather the given number is neon number or not i.e. 9 is number, 9**2=81→8+1=9

num=int(input('enter a number:'))
square=num**2
sum=0
while square!=0:
    dig=square%10
    sum+=dig
    square=square//10
if sum==num:
    print(f'{num} is a neon number')
else:
    print(f'{num} is a not neon number')