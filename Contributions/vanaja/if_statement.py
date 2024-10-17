# 1. check even number prg
num=int(input("enter the number : "))
if num%2==0:
    print(f"{num} is even number")

# 2.check  odd number prg
num=int(input("enter the number : "))
if num%2==1:
    print(f"{num} is odd number")

# 3. check given alpha is vowel
alpha=input("enter the alphabets")
if alpha in "aeiou AEIOU":
    print(f"{alpha} is vowel")

# 4 check value is single value data type
value=eval(input("enter the vale : "))
if type(value) in [int,float,complex,bool]:
    print(f"{value} is single value data type")

# 5 check set a is superset of setb
seta={1,2,3,4}
setb={2,3}
if seta.issuperset(setb):
    print(f"set a is superset of set b")

# 6 check set b is subset of set a
seta={1,2,3,4}
setb={2,3}
if setb.issubset(seta):
    print(f"set b is subset of set a")

# 7 check user enter word start with uppercase
word=input("enter the word : ")
first_letter=word[0]
if first_letter.isupper():
    print(f"in word {word} of  first letter {first_letter} is uppercase")

# 8 check user enter number is positive
num=int(input("enter the number : "))
if num>0:
    print(f"{num} is positive number")

# 9 check user enter number is multiple 5 and devisble by 3
num=int(input("enter the number : "))
if num%5==0 and num%3==0:
    print(f"{num} is multiple of 5 and 3")

# 10 check useer enter number is 3 digit number
num=int(input("enter the number : "))
if (99 < num <999)or(-999< num <-99)
    print(f"{num} is 3 digit number")

# 11 check user enter word is palindrome
word=input("enter the word : ")
rev_word=word[::-1]
if word==rev_word:
    print(f"the given {word} is palindorome")

# 12.Write a program To register.For a company only if job location is Bangalore.
location=input("enter the location : ")
if location=="bangalore":
    name=input("enter the name: ")
    phone_number=int(input("enter the mobile number"))
    print("you are registerd")

# 13.Write a program to check whether the given number lies between 5 to 10 
num=int(input("enter the number : "))
if 5 < num <10:
    print("number lies between 5 to 10")

# 14.Write a program To check whether the given string is having more than three characters 
string=input("enter the string : ")
if len(string)>3:
    print(f"{string} having more than three characters ")

# 15. Write a program.To check whether the given number is having.4 digits 
num=int(input("enter the number1 : "))
if (999< num <=9999) or (-9999< num <=-999):
    print(f"{num} is having 4 digits")

# 16.Write a program to check whether the given integer number is even and multiple of five
num=int(input("enter the number : "))
if num%2==0 and num%5==0:
    print(f"{num} is even and multiple of five")

# 17.Write a program.To check whether the given string is (single) character 
string=input("enter the string : ")
if len(string)==1:
       print(f"{string} is (single) character ")

# 18.Write a program.To check whether the given character is uppercase alphabet 
char=input("enter the charachter :")
if char.isupper():
    print(f"{char} is uppercase")

# 19.Write a program To check whether the given character is lowercase alphabet 
char=input("enter the charachter :")
if char.islower():
    print(f"{char} is lowercase")

# 20.Write a program to check whether the given character is digit 
char=input("enter the charachter :")
if char.isnumeric():
    print(f"{char} is digit")

# 21.Write a program to check whether the given character is alphabet 
char=input("enter the charachter :")
if char.isalpha():
    print(f"{char} is alphabets")

# 22.Write a program to check whether the given character is a special character
char=input("enter the charachter :")
if not char.isalnum():
    print(f"{char} is special character5")

# 23.Write a program to check whether the given collection is List 
collection=eval(input("enter the charachter :"))
if type(collection)==list:
    print(f"{collection} is list data type")

# 24.Write a program to check whether the entered value is default
value=eval(input("enter the charachter :"))
if value==" ":
    print(f"{value} is string data")
if value==[ ]:
    print(f"{value} is list data")
if value==( ):
    print(f"{value} is set data")
if value=={}:
    print(f"{value} is dict data")
if value==0:
    print(f"{value} is integer data")
if value==0.0:
    print(f"{value} is float data")
if value==False:
    print(f"{value} is bool data")

# 25.Write a program to check whether The list consists of even number of values 
collection=eval(input("enter the collection :"))
if len(collection)%2==0:
    print(f"{collection} has even number of values")

# 26.Write a program to check whether a list consists of middle value
collection=eval(input("enter the collection :"))
midlle_index=len(collection)//2
midlle_value=collection[midlle_index]
if midlle_value in collection:
    print(f"{midlle_value} is middle value of the list")

# 27.Write a program to check whether the entered input is.Immutable.   
value=eval(input("enter the value :"))
if type(value) in [str,tuple]:
    print(f"{value} is immutable data type")

# 28.Write a program to check whether the entered input is mutable.
value=eval(input("enter the value :"))
if type(value) not in [str,tuple]:
    print(f"{value} is mutable data type")

# 29.Write a program to check whether The entered input is a single value 
value=eval(input("enter the value :"))
if value in [int,float,complex,bool]:
    print(f"{value} is single value data type")

# 30.Write a program to check whether the entered input is multivalue or not.
value=eval(input("enter the value :"))
if value in [str,tuple,list,set,dict]:
    print(f"{value} is multi value data type")

# 31.Write a program to check whether the entered number is having only single Digit.
num=int(input("enter the number : "))
if -9<= num <=9:
    print(f"{num} is single digit")
