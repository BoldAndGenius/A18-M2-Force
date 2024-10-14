# Q85.Write a program to check weather the given number is automorphic or not I.e.5 is number 5**2=25 last digit of 25 is the number itself

# for single digit numbers

num=int(input('enter a single digit number:'))
if num>9:
    print('enter a single digit number:')
else:
    square=num**2
    if num==0:
        print(f'{num} is automorphic')
    else:
        while square!=0:
            last_digit=square%10
            break
        if last_digit==num:
            print(f'{num} is automorphic')
        else:
            print(f'{num} is not an automorphic')


# for all integers

num=int(input('enter a number:'))
square=num**2
str_num=str(num)
str_square=str(square)
if str_square.endswith(str_num):
    print('automorphic')
else:
    print('not an automorphic')