#Write a program To register for a company only if job location is Bangalore
location=input("Enter the location of job:")
if location == 'Bangalore':
    print("You have successfully registerd")

#Write a program to check whether the given number is even.
num=int(input("Enter a number:"))
if num % 2 == 0:
    print("It is even number")

#Write a program to check whether the given number is odd.
num=int(input("Enter a number:"))
if num % 2 == 1:
    print("It is odd number")
    
#Write a program to check whether the given number lies between 5 to 10.
num=int(input("Enter any number:"))
if 5 < num < 10:
    print("The number lies between 5 to 10")
    
#Write a program To check whether the given string is having more than three characters.
string=input("Enter a string:")
if len(string) > 3:
    print("string has more than three characters")

#Write a program to check whether the given number is having 4 digits.
num=int(input("Enter a number:"))
if 999 < num < 10000 or -999 > num > -10000:
    print("number is having 4 digits")

#Write a program to check whether the given character is a vowel.
character=input("Enter any character:")
if character in 'aeiouAEIOU':
    print("It belongs to vowel")

#Write a program to check whether the given integer number is even and multiple of five.
num=int(input("Enter a number:"))
if num % 2 == 0 and num % 5 == 0:
    print("number is even and multiple of 5 also")

#Write a program to check whether the given string is single character.
string=input("Enter a string:")
if len(string) == 1:
   print("yes it is single character")

#Write a program to check whether the given character is uppercase alphabet.
character=input("Enter any character:")
if character.isupper():
    print("Yes,character is uppercase alphabet.")

#Write a program To check whether the given character is lowercase alphabet.
character=input("Enter any character:")
if character.islower():
    print("Yes,character is lowercase alphabet.")

#Write a program to check whether the given character is digit.
character=input("Enter any character:")
if character.isnumeric():
    print("Yes,character is digit.")
    
#Write a program to check whether the given character is alphabet.
character=input("Enter any character:")
if character.isalpha():
    print("Yes,character is alphabet.")
    
#Write a program to check whether the given character is a special character.
character=input("Enter any character:")
if character.isalnum():
    print("it is not special character.")
    
#Write a program to check whether the given collection is List.
collection=eval(input("Enter a collection:"))
data_type=type(collection)
if data_type is list:
    print("it is list")

#Write a program to check whether the entered value is default.
value=eval(input("Enter a value:"))
if value in [0,0.0,0j,False,'',"",'''''',[],(),set(),{}]:
    print("yes it belongs to default value")
    
#Write a program to check whether the list consists of even number of values.
values = eval(input("Enter a list having atmost five values:"))

if len(values) % 2 == 0:
    print("The list consist of even number of values")

#Write a program to check whether a list consists of middle value.
list_ = eval(input("Enter a list:"))
if len(list_) % 2 == 1:
    print("list has middle value")

#Write a program to check whether the entered input is Immutable.
collection = eval(input("Enter a collection:"))
data_type = type(collection)
if data_type in [str,tuple]:
    print("given collection is immutable")

#Write a program to check whether the entered input is mutable.
collection = eval(input("Enter a collection:"))
data_type = type(collection)
if data_type in [list,set,dict]:
    print("given collection is mutable")
    
#Write a program to check whether The entered input is a single value DT.
input_ = eval(input("Enter a value:"))
data_type = type(input_)
if data_type in [int,float,complex,bool]:
    print("input belongs to single value data type")
    
#Write a program to check whether the entered input is multivalue DT or not.
input_ = eval(input("Enter a value:"))
data_type = type(input_)
if data_type in [str,list,tuple,set,dict]:
    print("input belongs to multi value data type")

#Write a program to check whether the entered number is having only single Digit.
num = int(input("Enter any number:"))
if 0 <= num <= 9:
    print("num is single digit")
