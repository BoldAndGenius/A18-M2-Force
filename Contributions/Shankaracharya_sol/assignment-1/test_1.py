#WAP to check whether a given character is vowel or consonent.if a given char is a vowel,store the char inside a list.If it is a consonent,display the ASCII value of the character.
character = input("Enter any character:")
if character in 'aeiouAEIOU':
    vowel_list = [character]
else:
    if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
        print(ord(character))
    
#WAP to check the greatest among 3 numbers entered by user using nested if.
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))
if num1 > num2:
    if num1 > num3:
        print("num1 is greater")
    else:
        print("num3 is greater")
else:
    if num2 > num3:
        print("num2 is greater")
    else:
        print("num3 is greater")
#WAP to check the type of type of traingle(equilateral,isosceles,scalene) usingnested if.
side1 = int(input("Enter side1:"))
side2 = int(input("Enter side2:"))
side3 = int(input("Enter side3:"))
if side1 == side2:
    if side1 == side3:
        print("Equilateral Traingle")
    else:
        print("isosceles traingle")
else:
    if side2 == side3:
        print("isoceles traingle")
    else:
        print("scalene traingle")
#Aceept no. of days from user & calculate library charge according to following criteria upto 5 days:5rs/day,6-10days:4rs/day,10-15days:3rs/day,more than 15days:3rs/day and display the total.
number_of_days = int(input("Enter number  of days:"))
if number_of_days <= 5:
    charge = 5
    total_charge = number_of_days * 5
    print(total_charge)
elif 5 < number_of_days <= 10:
    charge = 4
    total_charge = number_of_days * 4
    print(total_charge)
elif 10 < number_of_days <=15:
    charge = 3
    total_charge = number_of_days * 3
    print(total_charge)
else:
    charge = 2
    total_charge = number_of_days * 2
    print(total_charge)
