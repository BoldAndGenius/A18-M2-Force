#Write a program to check the relation between two integer numbers.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 == num2:
    print("Both are equal")
elif num1 > num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")
# Check for divisibility only if the numbers are not equal
if num1 != num2:
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2} and a multiple of {num2}")
    elif num2 % num1 == 0:
        print(f"{num2} is divisible by {num1} and a multiple of {num1}")
    else:
        print("No divisibility relation")


#Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it. 
character = input("Enter any character:")
if character.isupper():
    print("It is uppercase")
elif character.islower():
    print("It is lowercase")
elif character.isnumeric():
    print(f"it is numeric and ASCII value of {character} is {ord(character)}")

#Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.
character=input("Enter any character:")
if character in 'aeiouAEIOU':
    vowel_list=[character]
else:
    if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
        print(f"ASCII value of {character} is {ord(character)}")
        
#Write a program to check if the given data is individual data type or not. 
data = eval(input("Enter value:"))
if type(data) not in [int,float,bool,complex,str,list,tuple,dict,]:
    print("the given data is not a individual data type")
    
elif type(data) == int:
    print("it is of integer data type ")
    
elif type(data) == float:
    print("it is of float data type ")
    
elif type(data) == bool:
    print("it is of bool data type ")
    
elif type(data) == complex:
    print("it is of complex data type ")
    
elif type(data) == str:
    print("it is of string data type ")
    
elif type(data) == list:
    print("it is of list data type ")
    
elif type(data) == tuple:
    print("it is of tuple data type ")
    
elif type(data) == set:
    print("it is of set data type ")
    
elif type(data) == dict:
    print("it is of dictionary data type ")
    
#write a program to check whether the given integer single digit or two digits or three digits or more than three digits.
integer = int(input("Enter an integer:"))
if -9 <= integer <= 9:
    print("It's a single digit number")
elif -99 <= integer <= 99:
    print("It's a 2-digit number")
elif -999 <= integer <= 999:
    print("It's a 3-digit number")
else:
    print("It's more than 3-digit number")
    
#write a program to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5.
num = int(input("Enter an integer:"))
if num % 3 == 0 and num % 5 == 0:
    print("Fizzbuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print("Not a multiple of either 3 or 5")

#Write a program to predict grade of the student based on the obtained result .
result = float(input("Enter the result:"))
if result > 85:
    print("A+ Grade")
elif result > 70:
    print("A Grade")
elif result > 60:
    print("B Grade")
elif result > 40:
    print("C Grade")
elif result > 35:
    print("Just Passed")
else:
    print("Not Pass")

#Write a program to check whether the entered character is uppercase or lowercase or number or special character.
character = input("Enter a character:")
if character.isupper():
    print("Uppercase")
elif character.islower():
    print("Lowercase")
elif character.isnumeric():
    print("Nemeric")
else:
    print("Special character")

#Write a program to find the greatest among two numbers.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
if num1 > num2:
    print("num1 is greater")
elif num2 > num1:
    print("num2 is greater")
else:
    print("Both Numbers are equal")
    
#Write a program to find the smallest among three numbers.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
num3 = float(input("Enter num3:"))
if num1 < num2 and num1 < num3:
    print("num1 is smaller")
elif num2 < num1 and num2 < num3:
    print("num2 is smaller")
else:
    print("num3 is smaller")
    
#Write a program to find the greatest among four numbers.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
num3 = float(input("Enter num3:"))
num4 = float(input("Enter num4:"))
if num1 > num2 and num1 > num3 and num1 > num4:
    print("num1 is greater")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("num2 is greater")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("num3 is greater")
else:
    print("num4 is greater")
    
#Write a program to find the smallest among four numbers.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
num3 = float(input("Enter num3:"))
num4 = float(input("Enter num4:"))
if num1 < num2 and num1 < num3 and num1 < num4:
    print("num1 is smaller")
elif num2 < num1 and num2 < num3 and num2 < num4:
    print("num2 is smaller")
elif num3 < num1 and num3 < num2 and num3 < num4:
    print("num3 is smaller")
else:
    print("num4 is smaller")
#Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000.
units = float(input("Enter your electricity units:"))
if units <= 100:
    print("No charge")
elif units <= 200:
    charge = units * 5 
    print(f"The electricity bill is:{charge}")
elif 200 < units < 350:
    charge = units * 10
    print(f"The electricity bill is:{charge}")
else:
    print(f"The electricity bill is:2000")
    
#Write a program to accept percentages from the user and display the grade according to the following criteria. If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, gra inde is B if marks is greater than or equal to 60, and less than equals to 80 grade is C, else if it is less than 60 grade is D.
result = float(input("Enter the result %:"))
if result > 90:
    print("A Grade")
elif 90 <= result > 80:
    print("B Grade")
elif 80 <= result >= 60:
    print("C Grade")
elif result > 40:
    print("C Grade")
else:
    print("D Grade")
    
#Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria if cost price is greater than One Lac.The tax is 50%, if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% and if it is less than equals to 50,000 the tax is 5%.
cost_price = float(input("Enter cost price of bike:"))
if cost_price > 100000:
    tax = cost_price * (50/100)
    print(f"The road tax is:{tax}")
elif 50000 < cost_price <= 100000:
    tax = cost_price * (10/100)
    print(f"The road tax is:{tax}")
else:
    tax = cost_price * (5/100)
    print(f"The road tax is:{tax}")
    
#Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.
number = int(input("Enter a number from one to seven:"))
if number == 1:
    print("Sunday")
elif number == 2:
    print("Monday")
elif number == 3:
    print("Tuesday")
elif number == 4:
    print("Wednesday")
elif number == 5:
    print("Thursday")
elif number == 6:
    print("Friday")
else:
    print("Saturday")
    
#Write a program to accept a number from 1:00 to 12:00 and display name of the month and days in that month like one for January and number of days is 31 and so on.
number = int(input("Enter a number from 1 to 12:"))
if number == 1:
    print("The month is January and number of days is 31")
elif number == 2:
    print("The month is February and number of days is 29")
elif number == 3:
    print("The month is March and number of days is 31")
elif number == 4:
    print("The month is April and number of days is 30")
elif number == 5:
    print("The month is May and number of days is 31")
elif number == 6:
    print("The month is June and number of days is 30")
elif number == 7:
    print("The month is July and number of days is 31")
elif number == 8:
    print("The month is August and number of days is 31")    
elif number == 9:
    print("The month is September and number of days is 30")
elif number == 10:
    print("The month is October and number of days is 31")
elif number == 11:
    print("The month is November and number of days is 30")
else:
    print("The month is December and number of days is 31")
    
#Accept any city from the user and display monuments of that city. For Delhi it is Red Fort, Agra- Taj Mahal, Jaipur- Jal Mahal.
city = input("Enter any city from Delhi/Agra/Jaipur:")
if city == 'Delhi' or city == 'delhi':
    print("Red Fort")
elif city == 'Agra' or city == 'agra':
    print("Taj Mahal")
else:
    print("Jal Mahal")

#Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
side1 = int(input("Enter side1:"))
side2 = int(input("Enter side2:"))
side3 = int(input("Enter side3:"))
if side1 == side2 == side3:
    print("Equileteral Traingle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Traingle")
else:
    print("Scalene Traingle")
    
#Accept the number of days from the user and calculate the charge of library according to the following criteria. Till five days it is ₹2 per day, 6 to 10 days it is ₹3 per day, 11 to 15 days it is ₹4.00 per day and after 15 days it is five Rupees per day.
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
    
#Accept the kilometers covered and calculate the bill according to the following criteria. For 1st 10 kilometers it is ₹11.00 per kilometer, For next 90 kilometers it is rupees 10 per kilometer and after that it is ₹9 per kilometer.
distance = float(input("Enter kilometers covered:"))
if distance <= 10:
    bill = distance * 11
    print(f"The bill is:{bill}")
elif distance <= 100:
    bill = distance * 10
    print(f"The bill is:{bill}")
else:
    bill = distance * 9
    print(f"The bill is:{bill}")
    
#WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.
option = input("Choose the option from below\nA:Celsius to Kelvin\nB:Kelvin to Celsius\nEnter your option here:")
if option=='A':
        temperature = float(input("Enter the temperature:"))
        Kelvin = temperature + 273.15
        print(f"The temperature {temperature}\u00B0C is {Kelvin}K")
elif option=='B':
        temperature = float(input("Enter the temperature:"))
        celsius = temperature - 273.15
        print(f"The temperature {temperature}K is {celsius}\u00B0C")
else:
    print("Invalid Option")
