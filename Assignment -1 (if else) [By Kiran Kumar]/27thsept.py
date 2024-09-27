# Question - 87 
# Write a program to find the smallest among three numbers.

num1 = int(input("Enter number - 1 :"))
num2 = int(input("Enter number - 2 :"))
num3 = int(input("Enter number - 3 :"))

if (num1<num2) and (num1<num3):
    print(num1," is smallest")
elif (num2<num1) and (num2<num3):
    print(num2,"is smallest.") 
else:
    print(num3,"is samllest.")
    
    
    
# Question - 90
# Write a program to check whether a given character is vowel or consonant using nested if.

entered_character = input("Enter a character :").lower()
if entered_character == 'a':
    print("Vowel")
elif entered_character == 'e':
    print("Vowel")
elif entered_character == 'i':
    print("Vowel")
elif entered_character == '0':
    print("Vowel")
elif entered_character == 'u':
    print("Vowel")
else:
    print("Consonant")
   
   
   
   
   
# Question - 92 
# Write a program to check greatest among three numbers using nested if.

num1 = int(input("Enter a number - 1 :"))
num2 = int(input("Enter a number - 2 :"))
num3 = int(input("Enter a number - 3 :"))

if num1 > num2:
    if num1 > num3:
        print(num1, "is greatest.")
    else:
        print(num3, "is greatest.")
else:
    if num2 > num3:
        print(num2,"is greatest.")
    else:
        print(num3, "is greatest.")
        
        
        
# Question - 99
# WAP to check the type of a triangle (Equilateral,isosceles,scalene) using nested -if
side1 = int(input("Enter the Side - 1 :"))
side2 = int(input("Enter the Side - 2 :"))
side3 = int(input("Enter the Side - 3 :"))

if side1 == side2 == side3:
    print("Equilateral Triangle")
else:
    if (side1 == side2) or (side1==side3) or (side2 == side3):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")