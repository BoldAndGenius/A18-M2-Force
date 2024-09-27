# wap-- stands for write a program

#1.wap a program to print 'while loop' for 10 times
count=0
while count<10:
    print('while loop')
    count+=1

#2.wap a program to print first n natural numbers in one line
first=1
last=int(input('enter n value :'))
while first<=last:
    print(first,end=' ')
    first+=1

#3.wap a program to print first n whole numbers in one line
first=0
last=int(input('\nenter n value :'))
while first<last:
    print(first,end='   ')
    first+=1

#4.wap a program to print even numbers between 1 to 50
even=1
print("\nEven numbers")
while even<=50:
    if even%2==0:
        print(even)
    even+=1

#5.wap a program to print odd numbers between 1 to 50
odd=1
print("Odd numbers")
while odd<=50:
    if odd%2!=0:
        print(odd)
    odd+=1

#6.wap a program to print countdown of a game
count=10
print("\nstart countdowning")
while count>=0:
    print(count)
    count-=1

#7.wap to print items in a tuple using while loop
tuple1=eval(input('enter tuple of periodic elements'))
items=0
while items<len(tuple1):
    print(tuple1[items])
    items+=1

#8.wap to print items in a list using while loop
list1=eval(input('enter list of grocery items'))
items=0
while items<len(list1):
    print(list1[items])
    items+=1

#9.wap to print square of a  n numbers using while loop
square=0
last_square=int(input('enter last square number '))
while square<=last_square:
    print(square**2)
    square+=1

#10.wap to print cube of a  n numbers using while loop
cube=0
last_cube=int(input('enter last cube number '))
while cube<=last_cube:
    print(cube**3)
    cube+=1

#11.wap to print first 10 integers and their squares using while loop
first=1
last=10
while first<=last:
    print(first,first*first,sep=' ')
    first+=1

#12.write a while loop statement to print the following series 105,98,91,....,7
end=7
start=105
while start>=end:
    print(start)
    start-=7

#13.wap to print sum of first 10 natural numbers
sum=0
start=1
end=10
while start<=end:
    sum+=start
    start+=1
print(sum)

#14. wap to print sum of first 10 even numbers
sum=0
even=2
while even<=20:
    if even%2==0:
        sum+=even
    even+=2
print(sum)

#15.wap to print all even numbers that falls b/w two numbers (exclusive both numbers) entered by the user using while loop
start=int(input('enter starting number :'))
end=int(input('enter ending number :'))
while start<end:
    if start%2==0:
        print(start)
    start+=1

#16.wap to find sum of the digits of a number accepted from the user
sum=0
index=0
num=input('enter the number')
while index<len(num):
    sum+=int(num[index])
    index+=1
print(sum)

   # or

sum=0
remainder=0
num=int(input('enter the number'))
while num!=0:
    remainder=num%10
    sum=sum+remainder
    num//=10
print(sum)

#17.wap to find reverse of a number accepted from the user
reverse=0
remainder=0
num=int(input('enter number :'))
while num!=0:
    remainder=num%10
    reverse=reverse*10+remainder
    num//=10
print(reverse)

#18.wap to print the product of the digits of a number accepted from the user
num1=int(input('enter a number'))
product=1
remainder=0
while num1!=0:
    remainder=num1%10
    product=product*remainder
    num1//=10
print(product)

#19.wap to print the factorial of a number till n terms (accept input from user) using while loop
num=int(input('enter number'))
fact=1
start=1
if num>0:
    if num==0 or num==1:
        print(fact)
    else:
        while start<=num:
            fact=fact*start
            start+=1
print(fact)

#20.wap to check if a given word in list is palindrome or not ,if it is a palindrome append that word to new list
list1=['asha','asa',9,9.0,(1,'string'),[3,9,'a'],True,'radar']
index=0
list2=[]
while index<len(list1):
    string=list1[index]
    index+=1
    if type(string)== str:
        reverse=''
        index1=0
        while index1<len(string):
            char=string[index1]
            index1+=1
            reverse=char+reverse
        if reverse==string:
                list2.append(reverse)
print(list2)

#21.wap to mimic Upper mothod of string
string=input("enter a string :")
index=0
upper=''
while index<len(string):
    char=string[index]
    if 'A'<=char<='Z':
        upper+=char
    index+=1
print(upper)
# ( Or )
string=input("enter a string :")
index=0
upper=True
while index<len(string):
    char=string[index]
    if not('A'<=char<='Z'):
        upper=False
    index+=1
if upper==True:
    print("string contains only upper characters")
else:
    print("string contains otherthan upper characters")


#22.wap to mimic lower method of string
string=input("enter a string :")
index=0
lower=''
while index<len(string):
    char=string[index]
    if 'a'<=char<='z':
        lower+=char
    index+=1
print(lower)

 # (or)

string=input("enter a string :")
index=0
lower=True
while index<len(string):
    char=string[index]
    if not('a'<=char<='z'):
        lower=False
    index+=1
if lower==True:
    print("string contains only lower characters")
else:
    print("string contains otherthan lower characters")

#23.wap to mimic isnumeric method of string
num=input("enter a number :")
index=0
number=True
while index<len(num):
    digit=num[index]
    if not('0'<=digit<='9'):
        number=False
    index+=1
if number==True:
    print(f"{num} contains only digits")
else:
    print(f"{num} contains otherthan digits")

#24.wap to mimic string swapcase method
string=input('Enter a string with combination of uppercase and lowercase characters :')
index=0
ouput=''
while index<len(string):
    char=string[index]
    if char.islower():
        ouput+=char.upper()
    elif char.isupper():
        ouput+=char.lower()
    else:
        ouput+=char
    index+=1
print(ouput)

#25.wap to mimic replace method in string
line="GIVE RESPECT AND TAKE RESPECT"
index=0
output=''
while index<len(line):
    char=line[index]
    if char!=' ':
        output+=char
    else:
        output+="_"
    index+=1
print(output)

#26.wap to categorize the type of item in a user entered list are mutable or immutalbe
collection=eval(input('enter a list of items :'))
index=0
mutable=[]
immutable=[]
while index<len(collection):
    item=collection[index]
    if type(item) in [list,dict,set]:
        mutable.append(item)
    else:
        immutable.append(item)
    index+=1
print('Mutable list',mutable)
print('Immutable list',immutable)

#27.wap to extract all alphabets ,numbers and special characters from a given string using while loop
string=input('enter a string :')
alpha=''
numbers=''
special_char=''
index=0
while index<len(string):
    char=string[index]
    if char.isalpha():
        alpha+=char
    elif char.isnumeric():
        numbers+=char
    else:
        special_char+=char
    index+=1
print(f"Alphabets :{alpha},Numbers :{numbers},Special Characters :{special_char}")

#28.wap to check for a word palindrome without using slicing
word=input('Enter a word :')
index=0
reverse=''
while index<len(word):
    char=word[index]
    reverse=char+reverse
    index+=1
if reverse==word:
    print("Palindrome....")
else:
     print("Not a palindrome....")

#29.wap to extract all uppper and lower case characters from a given word using while loop 
word=input("Enter a word :")
index=0
lower=''
upper=''
while index<len(word):
    char=word[index]
    if char.isupper():
        upper+=char
    else:
        lower+=char
    index+=1
print(f"Uppercase string :{upper},Lowercase string :{lower}")

 #30.wap to check for a number palindrome without typecasting
reverse=0
remainder=0
num=int(input('enter number :'))
org_num=num
while num!=0:
    remainder=num%10
    reverse=reverse*10+remainder
    num//=10
if reverse==org_num:
    print('Palindrome....')
else:
    print('Not a palindrome....')

#31.wap to add all the digits in the user entered number only if it is an even number
num=int(input("Enter a Number :"))
sum=0
if num%2==0:
    while num!=0:
        last_digit=num%10
        sum=sum+last_digit
        num//=10
        index+=1
    print('sum :',sum)
else:
    print(f'{num} is not a even number,try with another number')

