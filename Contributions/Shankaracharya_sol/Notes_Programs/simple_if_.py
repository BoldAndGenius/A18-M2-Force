#WAP to check if the no. is even
num=int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is even")

#WAP to check if an alphabet is an vowel.
alphabet=input("Enter an alphabet:")
if alphabet in "aeiouAEIOU":
    print(f"{alphabet} is vowel")

#WAP to check if the user entered value is a single value data-type
data=eval(input("Enter a value:"))
type_of_data=type(data)
if type_of_data in [int,float,complex,bool]:
    print(f"{data} belongs to single value data type")

#WAP to check if the user entered word starts with an upper case character
word=input("Enter a word:")
upper=word[0]
if upper.isupper():
    print(f"Yes the '{word}' starts with upper case character")

#WAP to check if the user entered number is positive number
num=int(input("Enter a number:"))
if num >=0 :
    print("Yes it is positive number")

#WAP to check if the user entered number is multiple of 5 and divisible by 3
num=int(input("Enter a number:"))
if num % 5 == 0 and num % 3 == 0:
    print("It is multple of 5 and divisible by 3 also")

#WAP to check if the user entered number is a 3-digit number or not
num=int(input("Enter a number:"))
if 99 <= num <= 1000 or -99 >= num >= -1000:   #if (n>99 and n<1000) or (n<-99 and n>-1000)
    print("The number is a 3-digit number")

#WAP to check if the user entered set is a subset of another set
set1=eval(input("Enter set1:"))
set2=eval(input("Enter set2:"))
if set1.issubset(set2) or set2.issubset(set1):
    print("Yes it is subset")

#WAP to check if the user entered word is a palindrome
word=input("Enter a word:")
reverse_word=word[::-1]
if reverse_word == word:
    print("Its a palindrome")