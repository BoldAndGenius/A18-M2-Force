# 1. check the user enter num +ve or -ve & print
num=int(input("enter the number : "))
if num>=0:
    print(f"{num} is positive number")
else:
    print(f"{num} is negative number")

# 2. check user enter alpha is upper or lower
char=input("enter the charcter : ")
if char.isupper():
    print(f"{char} is upper case")
else:
    print(f"{char} is lowercase")

# without using build in function
char=input("enter the charcter : ")
if 'A'<= char <='Z':
    print(f"{char} is upper case")
else:
    print(f"{char} is lowercase")

# 3. CHECK USER ENTER char is special char or not
char=input("enter the charcter : ")
if not (char.isalnum()):
    print(f"{char} is special char")
else:
    print(f"{char} is not special char")

# without using build in function
char=input("enter the charcter : ")
if not(('A'<= char <='Z') or ('a'<= char<='z') or ('0'<=char <='9')):
    print(f"{char} is  special char")
else:
    print(f"{char} is not special char")

# 4.check if user enter data is muttable or immutable
value=eval(input("enter the value :"))
if type(value) in [list,tuple,set,dict]:
    print(f"{value} is mutable")
else:
    print(f"{value} is immutable")

# 5. check print square num  if user num is even else cube the num
num=int(input("enter the number : "))
if num%2==0:
    print(num**2)
else:
    print(num**3)

# 6. check user enter word is a keyword or not
import keyword
keyword=keyword.kwlist
word=input("enter the word : ")
if word in keyword:
    print(f"{word} is keyword")
else:
    print(f"{word} is not keyword")

# 7. check user enter collection is less than 5
collection=eval(input("enter the collection :"))
if len(collection)<=5:
    print(f"{collection} is less than 5")
else:
    print(f"{collection} is not less than 5")
 

# 8. check user enter data is single value or collection
data=eval(input("enter the data : "))
if type(data) in [int,float,complex,bool]:
    print(f"{data} is single value")
else:
    print(f"{data} is collection")  

# 9.check user data is vowel or constant
char=input("enter the charcter : ")
if char in 'aeiouAEIOU':
    print(f"{char} is vowel")
else:
    print(f"{char} is constant")

# 10.Write a program to check whether the first value present inside the given list is complex or not.
list=eval(input("enter the list: "))
if type(list[0]) in [complex]:
    print(f"{list[0]} is complex")
else:
    print(f"{list[0]} is not complex")

# 11..Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous
tuple_values=eval(input("enter the two tuple value: "))
if type(tuple_values) in [tuple]  and len(tuple_values)==2:
    if type(tuple_values[0])==type(tuple_values[1]):
        print(f"{tuple_values} is homogenous")
    else:
        print(f"{tuple_values} is hetrogeneous")
else:
    print(f"{tuple_values} is not tuple")

# 12.Write a program to check whether the given integer number is multiple of 10 or not.
integer=int(input("enter the integer value: "))
if integer%10==0:
    print(f"{integer} is multiple of 10")
else:
    print(f"{integer} is not multiple of 10")

# 13.Write a program to check whether the given string is palindrome or not.
string=input("enter the string : ")
rev_word=string[::-1]
if string==rev_word:
    print(f"{rev_word} is pallindrome")
else:
    print(f"{rev_word} is not pallindrome")

# 14.Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.
string=input("enter the string: ")
if len(string) >=3:
    print(f"length of the string is {len(string)}")
else:
    print(f"string is {string}")

# 15.Write a program to check whether the user is eligible to vote or not
age=int(input("enter the age :"))
if age>=18:
    print("you are eligible to vote")
else:
    print("your not eligebale for vote")

# 16.Write a program to check whether a number is divisible by 7 or not.
integer=int(input("enter the integer value: "))
if integer%7==0:
    print(f"{integer} is divisible of 7")
else:
    print(f"{integer} is not divisible of 7")

# 17.Write a program to check whether the last digit of a number entered by the user is divisible by three or not.
digits=int(input("enter the digits"))
if digits %10%3==0:
    print("it is divible by 3")
else:
    print("it is not divible by 3")

# 18.Write a program to check whether the year is leap year or not.
year = int(input("Enter year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 19.Write a program to check whether a number entered is a 3 digit number or not.
number=int(input("enter the number: "))
if (number>=100 and number<=999) or (number<=-100 and number>=-999):
    print("it is 3 digit number")
else:
    print("it is not 3 digit number")

# 20.Write a program to find the largest number out of two numbers expected from the user.
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if num1>num2:
    print(f"{num1} is largest number")
else:
    print(f"{num2} is largest number")

# 21.Write a program.To check whether a number accepted from the user is divisible by two and three both.
digits=int(input("enter the digits"))
if digits%2==0 and digits%3==0:
    print("it is divible by 3")
else:
    print("it is not divible by 3")
