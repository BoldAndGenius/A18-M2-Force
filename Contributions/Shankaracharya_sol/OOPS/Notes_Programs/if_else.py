#WAP to check if the user entered number is positive number and print accordingly.
num=int(input("Enter a number:"))
if num >= 0:
    print("It is Positive number")
else:
    print("It is Negative number")
    
#WAP to check if the user entered alphabet is uppercase or lowercase.
char=input("Enter a char:")
if 'a' <= char <= 'z':
    print("Lowercase")         #if char.isupper():
else:
    print("Uppercase")

#WAP to check if the user entered char is a special char or not and print accordingly
char=input("Enter a char:")
if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
    print("Not a special character")
else:
    print("Special Character")


#WAP to check if the user entered data is mutable or immutable
data=eval(input("Enter a value:"))
type_of_data=type(data)
if type_of_data in [list,set,dict]:
    print(f"{type_of_data} is Mutable")
else:
    print(f"{type_of_data} is immutable")

#WAP to print sqaure of a number if the user entered number is even else print cube of the number.
num=int(input("Enter a number:"))
if num % 2 == 0:
    square=num**2
    print(f"The square of {num} is {square}")
else:
    cube=num**3
    print(f"The cube of {num} is {cube}")

#WAP to check if the user entered word is keyword or not
import keyword
word=input("Enter any word:")
if word in keyword.kwlist:
    print(f"{word} is a keyword")
else:
    print(f"{word} is not a keyword")

#WAP to check if the user entered data is single value data type or collection data type
data=eval(input("Enter any value:"))
if type(data) in [int,float,complex,bool]:
    print(f"{data} belongs to SVDT")
else:
    print(f"{data} belongs to collection")

#WAP to check if the user entered collection has less than 5 element
collection=eval(input("Enter any collection:"))
if len(collection) <= 5:
    print(f"{collection} has less than or equal to 5 element")
else:
    print(f"{collection} has more than 5 element")