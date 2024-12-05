#WAP to ask marks from the user and print pass type accordingly
marks=int(input("Enter marks:"))
if marks >= 85:
    print("Distinction")
elif marks >= 70:
    print("First Class")
elif marks >= 60:
    print("Second Class")
elif marks >=35:
    print("just pass")
else:
    print("Not passed")

#WAP to print the type of character entered by user
character=input("Enter any character:")
if 'A' <= character <= 'Z':           #using built in method----character.isupper()
    print(f"{character} is Uppercase")
elif 'a' <=character <= 'z':          #using built in method----character.islower()
    print(f"{character} is Lowercase")
elif '0' <= character <= '9':         #using built in method----character.isnumeric() or character.isdigit()
    print(f"{character} is numeric")
else:                                 #using built in methods----character.isalnum()
    print(f"{character} is special character")
    

#WAP to check whether two sets are subsets,equal sets,disjoint or no relation between the set and sets are entered by the user
set1=eval(input("Enter set1:"))
set2=eval(input("Enter set2:"))

if set1 < set2:                     #using built in method----set1.issubset(set2)
    print("set1 is subset of set2")
elif set2 < set1:                   #using built in method----set2.issubset(set1)
    print("set2 is subset of set1")
elif set1 == set2:                  #No built in method to check two sets equal
    print("Equal Sets")
elif set1 & set2 == set():          #using built in method----set1.isdisjoint(set2)
    print("disjoint sets")
else:
    print("No relation between the sets")
    
#WAP to check whether two numbers are greater than or less than or equal to each other
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both are equal numbers")
    

#WAP to check if the user entered number is single digit or 2-digit or 3-digit or more than that.
digit=int(input("Enter an integer:"))
num=digit
if digit < 0:
    digit=-digit
if len(str(digit)) == 1:
    print(f"{num} is single digit number")
elif len(str(digit)) == 2:
    print(f"{num} is 2-digit number")
elif len(str(digit)) == 3:
    print(f"{num} is 3-digit number")
else:
    print(f"{num} is greater than 3-digit number")
############################       ONE MORE WAY   ###############################################
digit=int(input("Enter an integer:"))
if -9 <= digit <= 9:
    print(f"{digit} is single digit number")
elif -99 <= digit <= 99:
    print(f"{digit} is two digit number")
elif -999 <= digit <= 999:
    print(f"{digit} is three digit number")
else:
    print(f"{digit} is greater than thre digit number")

#WAP to find the greatest among three number entered by the user
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
if num1 == num2 == num3:
    print("all numbers are equal")
elif num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}")
else:
     print(f"{num3} is greater than {num1} and {num2}")
    

#wap to check if the three sides of traingle entered by the user is an equilateral,isosceles or scalene traingle
side1=int(input("Enter side1:"))
side2=int(input("Enter side2:"))
side3=int(input("Enter side3:"))

if side1 == side2 == side3:
    print("Equilateral Traingle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Traingle")
    
#WAP to check the bonus of an employee based on his experience
experience=int(input("Enter the experince of an employee:"))
sal=int(input("Enter the salary of that employee:"))
if experience <=2 :
    bonus=(sal*10)/100
    print(f"{bonus} is bonus")
elif 2 < experience <= 5:
    bonus=(sal*20)/100
    print(f"{bonus} is bonus")
else:
    bonus=(sal*25)/100
    print(f"{bonus} is bonus")