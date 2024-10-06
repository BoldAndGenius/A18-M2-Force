# 1. Write a program to print the square of a given integer number.

num = int(input("Enter a interger: "))
square = num ** 2
print(square)

# 2. Write a program to find the product of two float numbers.

num1 = float(input("Enter a float number: "))
num2 = float(input("Enter a float number: "))
product = num1 * num2
print(product)

# 3. Write a program to find the area of a rectangle.

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length*width
print(area)

# 4. Write a program to reverse the given string.

String = input("Enter a string: ")
reverse = String[::-1]
print(reverse)

# 5. Write a Program to find the sum, difference, product and division.Between 2 integer numbers.

num1 = int(input("Enter a integer: "))
num2 = int(input("Enter a integer: "))
sum = num1 + num2
diff = num1 - num2
product = num1 * num2
div = num1/num2
print(sum,diff,product,div)

# 6. Write a program to find the simple interest.

p = int(input("Enter a principle: "))
t = int(input("Enter a time: "))
r = int(input("Enter a rate: "))
si = (p*t*r)/100
print(si)

# 7. Write a program to calculate area of triangle

b = int(input("Enter a breadth: "))
h = int(input("Enter a height: "))
area_triangle = 1/2*b*h
print(area_triangle)

# 8. Write a Python code to swap two variables.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
a,b=b,a
print("Swapped values: a=", a,"b=",b)

# 9. Write a Python program to calculate the square root of a given number

num = float(input("Enter Number: "))
square_root = num**0.5
print(square_root)

# 10. Write a Python program to find the area of a circle.

radius = int(input("Enter a radius: "))
area_circle = 3.14*(radius**2)
print(area_circle)

# 11.Write a program To register.For a company only if job location is
# Bangalore.

name = input("Enter Name: ")
email = input("Enter email: ")
location = input("Enter Location: ")
if location.upper() == "banglore":
    print("Register Succesfully!")

# 12. Write a program to check whether the given number is even

num =  int(input("Enter a number: "))
if num%2 == 0:
    print(" Even Number ")

# 13. Write a program to check whether the given number is odd

num = int(input("Enter a number: "))
if num%2 != 0:
    print("Odd Number")

# 14. Write a program to check whether the given number lies between 5 to 10

num = int(input("Enter b/w 5 to 10: "))
if 5<=num<=10:
    print("Satisfied")

# 15. Write a program To check whether the given string is having more than three characters

string = input("Enter a string: ")
if len(string) > 3:
    print("More than 3 characters")

# 16. Write a program.To check whether the given number is having.4 digits

num = int(input("Enter a Number: "))
if (1000<=num<=9999) or (-1000>=num>=-9999):
    print("Having 4 digits")

# 17. Write a program to check whether the given character is a vowel

alpha = input("Enter a alpha: ")
if alpha in "aeiouAEIOU":
    print(f"{alpha} is a Vowel")
    
# 18. Write a program to check whether the given integer number is even and multiple of five    
    
num = int(input("Enter a Number: "))
if num%2==0 and num%5==0:
    print("It is even and mulptiply by 5")

# 19. Write a program.To check whether the given string is (single) character

string = input("Enter a char: ")
if len(string)==1:
    print("it is a single character")

# 20. Write a program.To check whether the given character is uppercase alphabet

string = input("Enter a char: ")
if string.isupper():
    print("Yes Uppercase")

# 21. Write a program.To check whether the given character is lowercase alphabet

string = input("Enter a string: ")
if string.islower():
    print("Lowercase Bayya")

# 22. Write a program to check whether the given character is digit

digit = input("Enter a number: ")
if digit.isnumeric():
    print("Number bayya")

# 23. Write a program to check whether the given character is alphabet

alpha = input("Enter a alphabet: ")
if alpha.isalpha():
    print("It is a alphabet")

# 24. Write a program to check whether the given character is a special character

char = input("Enter a character: ")
if not char.isalnum():
    print("Special Character")
    
# 25. Write a program to check whether the given collection is List

list1 = eval(input("Enter a list: "))
if type(list1) == list:
    print("Collection is list")

# 26. Write a program to check whether the entered value is default

value = eval(input("Enter a Value: "))
if bool(value) == False:
    print("Default Value")
    
# 27. Write a program to check whether The list consists of even number of values

my_list1 = eval(input("Enter a list: "))
if len(my_list1)%2 == 0:
    print("The list have even number of values")
    
# 28. Write a program to check whether a list consists of middle value

my_list1 = eval(input("Enter a list: "))
if len(my_list1)%2 != 0:
    print("list have middle Value")
     
# 29. Write a program to check whether the entered input is.Immutable.

data = eval(input("Enter a data: "))
if type(data)  not in [list,set,dict]:
    print("IMMutable")

# 30. Write a program to check whether the entered input is mutable.

data = eval(input("Enter a data: "))
if type(data) in [list,set,dict]:
    print("Muttable")

# 31. Write a program to check whether The entered input is a single value

data = eval(input("Enter a data: "))
if type(data) in [int,float,bool,complex]:
    print("single Value datatype")

# 32. Write a program to check whether the entered input is multivalue or not.

data = eval(input("Enter a data: "))
if type(data) in [str,list,tuple,set,dict]
    print("Multi value")

# 33. Write a program to check whether the entered number is having only single Digit.

data = int(input("Enter a number: "))
if -9<=data<=9:
    print("single digit")
    
# 34. Uni whether the first value present inside the given list is complex or not.

list1 = eval(input("Enter a list: "))
check = list1[0]
if type(check) == complex:
    print("First value is Complex")
else:
    print(" First value is Not complex")

# 35. Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.

tuple1 = eval(input("Enter a collection: "))
if len(tuple1) == 2:
    print("Exactly 2 values")
if type(tuple1[0])==type(tuple1[1]):
    print("Homogenous")
else:
    print("Heterogenus")
    
# 36. Write a program to check whether the given integer number is multipleof 10 or not.

num = int(input("Enter a number: "))
if num%10 == 0:
    print("multiply by 10")
else:
    print("Not Multiply by 10")
    
# 37. Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number.

num = int(input("enter a Number: "))
if num%2==0:
    print(f"{num**2}")
else:
    print(f"{num**3}")
    
# 38. Write a program to check whether the given string is palindrome or not.

string = input("Enter a string: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# 39. Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.

string = input("Enter a character: ")
if len(string)>3:
    print(len(string))
else:
    print(string)

# 40. Write a program to check whether the user is eligible to vote or not.

age = int(input("Enter a age:")) 
if age>=18:
    print("You can Vote") 
else:
    print("You have Not Vote Buddy")

# 41. Write a program to check whether a number is divisible by 7 or not.

num = int(input("Enter a number: "))
if num%7 == 0:
    print("Divisible by 7")
else:
    print("Not divisble by 7")

# 42. Write a program to check whether the last digit of a number entered by the user is divisible by three or not.

num = int(input("Enter a Number: "))
if num%10%3==0:
    print("Last digit Divisible by 3")
else:
    print("Last digit Not divisble by 3")

# 43. Write a program to check whether the year is leap year or not.

year = int(input("Enter a year: "))
if year%4==0 and (year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Not leap year")

# 44. Write a program to check whether a number entered is a 3 digit number or not.

num = int(input("Enter Number: "))
if -999<=num<=-100 or 100<=num<=999:
    print("Number has 3 digits")
else:
    print("Number not have 3 digits")

# 45. Write a program to find the largest number out of two numbers expected from the user.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1>num2:
    print("Num1 is greatest")
else:
    print("Num2 is greatest")
    
# 46. Write a program to check whether a number.Entered by the user is positive or negative.

num = int(input("Enter a number: "))
if num>0:
    print("Positive Number")
else:
    print("Negative Number")
    
# 47. Write a program.To check whether a number accepted from the user is divisible by two and three both.

num = int(input("Enter Number: "))
if num%2==0 and num%3==0:
    print("Number divisble by both 2 and 3")
else:
    print("Not divisble by both")
    
# 48. Write a program to check the relation between two integer numbers

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
if a==b:
    print("Both Equal")
elif a>b:
    print("A is Greatest")
else:
    print("B is greatest")
    
# 49. Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If
# character is lowercase print lowercase. If the character is a number, print the ascii number of it.

char = input("Enter Character: ")
if char.isalpha():
    if char.isupper():
        print("uppercase")
    else:
        print("lowercase")
elif char.isnumeric():
    print(ord(char))
else:
    print("special Character")
    
# 50. Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the
# list. If a given character is consonant, display the ASCII value of that character.    

char = input(input("Enter character: "))
if char in "aeiouAEIOU":
    print([char])
else:
    print(ord(char))
    
# 51. Write a program to check if the given data is individual data type or not.

data = eval(input("Enter data: "))
if data in [int,float,complex,bool]:
    print("individual data type")
else:
    print("not individual data type")
    
# 52. write a program to check whether the given integer single digit or two digits or three digits or more than three digits

num = int(input("Enter a Number: "))
if -9<=num<=9:
    print("single digit")
elif -99<=num<=99:
    print("Two digit number")
elif -999<=num<=999:
    print("Three digit")
else:
    print("More than 3 digit")
    
# 53. write a program to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the
# number is multiple of both 3 and 5

num = int(input("Enter Number: "))
if num%3 == 0:
    print("Fizz")
elif num%5==0:
    print("buzz")
elif num%3 == 0 and num%5 == 0:
    print("Fizzbuzz")
else:
    print("Not multiple 3 and 5")
    
# 54. Write a program to predict grade of the student based on the obtained result

result = int(input("Enter Marks: "))
if result>900:
    print("A grade")
elif result>800:
    print("B grade")
elif result>700:
    print("C grade")
elif result>600:
    print("D grade")
elif result>500:
    print("E grade")
else:
    print("Fail")
    
# 55. Write a program to check whether the entered character is uppercase or lowercase or number or special character

char = input("Enter character: ")
if char.isupper():
    print("Given char is uppercase")
elif char.islower():
    print("Given char is lowercase")
elif '0'<=char<='9':
    print("Given char is Number")
else:
    print("Given char is special charracter")
    
# 56. Write a program to find the greatest among two numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1>num2:
    print("Num1 is grreatest")
elif num2>num1:
    print("Num2 is greatest")
else:
    print("Both equal")

# 57. Write a program to find the smallest among three numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1<num2:
    if num1<num3:
        print("Num1 is smallest")
    else:
        print("Num3 is smallest")
else:
    if num2<num3:
        print("Num2 is smallest")
    else:
        print("num3 is smallest")
        
# 58. Write a program to find the greatest among four numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
if num1>num2 and num1>num3 and num1>num4:
    print("Num1 is greatest")
elif num2>num1 and num2>num3 and num2>num4:
    print("Num2 is greatest")
elif num3>num1 and num3>num2 and num3>num4:
    print("Num3 is greatest")
elif num4>num1 and num4>num2 and num4>num3:
    print("Num4 is greatest")
elif num1==num2:
    print("Both 1 and 2 equal and greatest")
elif num1==num3:
    print("Both 1 and 3 equal and greatest")
elif num1==num4:
    print("Both 1 and 4 equal and grestest")
elif num2==num3:
    print("Both 3 and 3 equal and grestest")
elif num2==num4:
    print("Both 2 and 4 equal and grestest")
else:
    print("Both 3 and 4 equal and grestest") 

# 59. Write a program to find the smallest among four numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
if num1<num2 and num1<num3 and num1<num4:
    print("Num1 is smallest")
elif num2<num1 and num2<num3 and num2<num4:
    print("Num2 is smallest")
elif num3<num1 and num3<num2 and num3<num4:
    print("Num3 is smallest")
elif num4<num1 and num4<num2 and num4<num3:
    print("Num4 is smallest")
elif num1==num2:
    print("Both 1 and 2 equal and small")
elif num1==num3:
    print("Both 1 and 3 equal and small")
elif num1==num4:
    print("Both 1 and 4 equal and small")
elif num2==num3:
    print("Both 3 and 3 equal and small")
elif num2==num4:
    print("Both 2 and 4 equal and small")
else:
    print("Both 3 and 4 equal and small") 
        
        
# 60. Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5
# per unit and after 200 units, the price is rupees 10 per unit.If the input is
# 350 then total bill amount is Rupees 2000.

bill = float(input("Enter a bill: "))
if bill<=100:
    print("No charge")
elif bill<=200:
    print((bill-100)*5)
elif bill<=400:
    print((bill-200)*10+100*5)
else:
    print("You consult manager bcz your spend more..")
   
# 61. Write a program to accept percentages from the user and display the grade according to the following criteria. If marks is greater than 90, grade
# is A. If marks is greater than 80 and less than equals to 90, gra inde is B if marks is greater than or equal to 60, and less than equals to 80 grade is C,
# else if it is less than 60 grade is D

marks = int(input("Enter the marks: "))
if marks >= 90:
    print("A grade")
elif 80< marks <=90:
    print("B grade")
elif 60< marks <=80:
    print("C grade")
else:
    print("D grade")
    
# 62. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria if cost price is greater than
# One Lac.The tax is 50%, if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% and if it is less than equals to 50,000 the tax is 5%.

cost = int(input("Enter a Bike Cost: "))
if cost > 100000:
    print(f"The tax is {(cost*50)/100}")
elif cost > 50000:
    print(f"The tax is {(cost*10)/100}")
else:
    print(f"The tax is {(cost*5)/100}")

# 63. Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.

num = int(input("Enter a number: "))
if 1<=num<=7:
    if num==1:
        print("Sunday")
    elif num==2:
        print("Monday")
    elif num==3:
        print("Tuesday")
    elif num==4:
        print("Wednesday")
    elif num==5:
        print("Thursday")
    elif num==6:
        print("Friday")
    else:
        print("Saturday")
else:
    print("Invalid Number")
    
# 64. Write a program to accept a number from 1:00 to 12:00 and display name of the month and days in that month like one for January and
# number of days is 31 and so on.

num = int(input("Enter Number: "))
if 1<=num<=12:
    if num==1:
        print("January and 31 days")
    elif num==2:
        print("February and 28/29 days")
    elif num==3:
        print("March and 31 days")
    elif num==4:
        print("April and 30 days")    
    elif num==5:
        print("May and 31 days")
    elif num==6:
        print("June and 30 days")
    elif num==7:
        print("July and 31 days")
    elif num==8:
        print("August and 31 days")
    elif num==9:
        print("September and 30 days")
    elif num==10:
        print("October and 31 days")
    elif num==11:
        print("November and 30 days")
    else:
        print("December and 31 days")
else:
    print("Invalid")
        
# 65. Accept any city from the user and display monuments of that city. For Delhi it is Red Fort, Agra- Taj Mahal, Jaipur- Jal Mahal.

city = {"Delhi":"Redfort","Agra":"Taj","AP":"Amaravati","Hyd":"Amazon"}
which = input("Enter any city: ")
if which in city:
    print(city[which])
else:
    print("Not Here")
    
# 66. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

s1 = float(input("Enter a side1: "))
s2 = float(input("Enter a side2: "))
s3 = float(input("Enter a side3: "))
if s1==s2==s3:
    print("Equi Triangle")
elif s1 != s2 != s3:
    print("Scalene Triangle")
else:
    print("Iscoceles Triangle")
    
# 67. Accept the number of days from the user and calculate the charge of library according to the following criteria. Till five days it is ₹2 per day, 6 to
# 10 days it is ₹3 per day, 11 to 15 days it is ₹4.00 per day and after 15 days it is five Rupees per day.

num_of_days = int(input("Enter a days: "))
if num_of_days<=5:
    print(num_of_days*2)
elif num_of_days<=10:
    print(num_of_days*3)
elif num_of_days<=15:
    print(num_of_days*4)
else:
    print(num_of_days*5)
    
# 68. Accept the kilometers covered and calculate the bill according to the following criteria. For 1st 10 kilometers it is ₹11.00 per kilometer, For next
# 90 kilometers it is rupees 10 per kilometer and after that it is ₹9 per kilometer.

km = float(input("Enter a Kilometers: "))
if km<=10:
    print(f"{km} bill is {km*11}")
elif km<=100:
    print(f"{km} bill is {(km-10)*10 + (10*11)}")
else:
    print(f"{km} bill is {(km-100)*9+(90*10) +(10*11)}")
    
    
# 69. WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.

choice = input("Select 'C' Celsius to kelvin and 'K' kelvin to Celsius: ")
if choice.upper() == 'C': 
    C = float(input("Enter a temp: "))
    kelvin = C + 273.15
    print(kelvin)
elif choice.upper() == 'K':
    K = float(input("Enter a Kelvin temp: "))
    celsius = K-273.15
    print(celsius)
else:
    print("invalid")
    
# 70. Write a program to create an Instagram login page.

data = {"manoj":"Manoj9835@","yatheeshreddy":"Yathesh12","lokeswar_reddy":"Lokesh@09","Sai":"sai01@"}
username = input("Enter username:")
password = input("Enter password: ")
if username in data:
    actual_pw = data[username]
    if password == actual_pw:
        print("Login succesfully")
    else:
        print("wronng Password")
else:
    print("Not exist user details")
    
# 71. Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater
# than 3

tup1 = ("Man",21,"sam",3+5j,4.2,34,45)
if len(tup1)>3:
    middle_value=len(tup1)//2
    if type(tup1[middle_value]) == str:
        print(tup1[middle_value])
    else:
        print("its not string")
else:
    print("Length more than not 3")
    
# 72. Write a program.To check the greater among four numbers using nested if.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))
if a>b:
    if a>c:
        if a>d:
            print("A is greatest")
        else:
            print("D is greatest")
    else:
        if c>d:
            print("C is greatest")
        else:
            print("D is geatest")
else:
    if b>c:
        if b>d:
            print("B is greatest")
        else:
            print("D is greatest")
    else:
        if c>d:
            print("C is Greatest")
        else:
            print("D is grestest")

# 74. Write a program to find the second greatest among four numbers.

a=int(input("Enter Number: "))
b=int(input("Enter Number: "))
c=int(input("Enter Number: "))
d=int(input("Enter Number: "))
if a>b:
    if a>c:
        if a>d:
          if d>b and d>c:
              print(" d is 2nd largest")
          elif b>d and b>c:
              print(" b is 2nd largest")
          else:
              print("c is 2nd largest")
        else:
            if a>b and a>c:
                print("a is 2nd largest")
            elif b>c and b>d:
                print("b is 2nd largest")
            else:
                print("c is 2nd largest")
    else:
        if c>d:
            if d>a and d>b:
                print("d is 2nd largest")
            elif b>a and b>d:
                print("b is 2nd largest")
            else:
                print("a is 2nd largest")
        else:
            if c>a and c>b:
                print("c is 2nd largest")
            elif a>c and a>b:
                print("a is 2nd largest")
            else:
                print("b is 2nd largest")
else:
    if b>c:
        if b>d:
            if d>a and d>c:
                print("d is 2nd largest")
            elif c>a and c>d:
                print(" c is 2nd largest")
            else:
                print("a is 2nd largest")
        else:
            if b>a and b>c:
                print("b is 2nd Largest")
            elif a>c and a>d:
                print("a is 2nd largest")
            else:
                print("c is 2nd largest")
    else:
        if c>d:
            if d>a and d>b:
                print("d is 2nd largest")
            elif a>b and a>d:
                print(" a is 2nd largest")
            else:
                print("b is 2nd largest")
        else:
            if c>a and c>b:
                print("c is 2nd largest")
            elif b>a and b>c:
                print("b is 2nd largest")
            else:
                print("a is 2nd largest")

# 75. Write a program.To check the type of a given character.

char = input("Enter character: ")
if char.isalpha():
    if char.islower():
        print("Character is lowercase alphabeT")
    else:
        print("Character is uppercase alphabet")
elif char.isnumeric():
    print("Character is Numeric")
else:
    print("Character is Special Characcter")

# 76. Write a program to consider an integer number. Print happy if the number is divisible by two. Print SAD if the number is divisible by 5 and
# print square of the numbers only if it is divisible by seven else print the number as it is.

num = int(input("Enter a Number: "))
if num%2 == 0:
    print("happy")
elif num%5 == 0:
    print("SAD")
elif num%7 == 0:
    print(f"Sqaure of Number is {num**2}.")
else:
    print(num)
    
# 77. Write a program to find the smallest among three numbers.

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
num3 = int(input("Enter a number3: "))
if num1<num2:
    if num1<num3:
        print("Number1 is smallest")
    else:
        print("Number 3 is smallest")
else:
    if num2<num3:
        print("Number2 is smallest")
    else:
        print("Number3 is smallest")
        
# 78. Program to consider an input string. Print the string as it is if it is palindrome. Print the reverse string if it has an even number of characters.
# Print all the characters present at an odd index if the string is having an odd number of characters.

string = input("Enter a word: ")
if string == string[::-1]:
    print(string)
elif len(string)%2 == 0:
    print(string[::-1])
else:
    print(string[1::2])
    
# 79. Write a program to print middle Character.Given string only if it is upper case character.

word = input("enter a string: ")
if len(word)%2 !=  0:
    mid_value = round(len(word)//2)
    if word[mid_value].isupper():
        print(f"{word[mid_value]} is upper")
    else:
        print("Middle is not uppercase")
else:
    print("Even characters not defined middle value")
    
# 80. Write a program to check whether a given character is vowel or consonant using nested if.

char = input("Enter a character: ")
if char.isalpha():
    if char in "aeiouAEIOU":
        print("Char is vowel")
    else:
        print("Char is Consonant")
else:
    print("It's not a alpabet")
    
# 81. Write a program to print the length of given data only if it is even.

data = eval(input("enter data: "))
if len(data)%2==0:
    print(len(data))
else:
    print("data has not even")
    
# 82. Write a program to check greatest among three numbers using nested if.

x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
z = int(input("Enter number3: "))
if x>y:
    if x>z:
        print("X is greatest")
    else:
        print("z is greatest")
else:
    if y>z:
        print("y is greatest")
    else:
        print("z is greatest")
        
# 83. Write a program.To check second greatest among three numbers using nested if.

x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
z = int(input("Enter number3: "))
if x>y:
    if x>z:
        if z>y:
            print("Z is 2nd greatest")
        else:
            print("y is 2nd greatest")
    else:
       print("x is 2nd greatest")
else:
    if y>z:
        if z>x:
            print("z is 2nd greatest")
        else:
            print("x is 2nd greatest")
    else:
        print("y is 2nd greatest") 
           
# 84. Write a program that determines the movie ticket price based on the age and day of the week
# Adults (18+): $12 (except for Tuesdays: $10)
# Children (under 18): $8 (except for Tuesdays: $6)
# Seniors (65+): $8 (always)

age = int(input("Enter age: "))
day = input("Enter day: ")
if age<18:
    if day != "Tuesday" or "tuesday":
        print("Your ticket price is $6")
    else:
        print("Your ticket price is $8")
elif 18<=age<=65:
    if day != "Tuesday" or "tuesday":
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $12")
else:
    print("Your ticket price is $8")
   
# 85. Leap Year Checker: Write a program that determines if a given year is a leap year. A leap year is a year divisible by 4, but not by 100 unless it's
# also divisible by 400.

year = int(input("Enter year: "))
if year%4==0:
    if year%400==0:
        if year%100!=0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap")

# 86. Vending Machine: Create a program for a vending machine that take-s product code (integer) and amount paid (float) as input. It should check the product price (stored in a dictionary) and dispense the product if enough is paid. Use nested ifs for different error messages (e.g., invalid code,insufficient funds).








    
# 87. Restaurant Discount: Write a program that calculates a restaurant bill with a discount based on the day of the week and party size:
# Weekdays (Mon-Fri), party < 4: No discount.
# Weekdays (Mon-Fri), party >= 4: 10% discount.
# Weekends (Sat-Sun), any party size: 15% discount.

party_size = int(input("Enter size: "))
day = input("Enter day: ")
bill = int(input("Enter bill: "))
if day.lower() in ["monday","tuesday","wednesday","thursday","friday"]:
    if party_size >= 4:
        print(f"Your bill is {bill-(bill*0.10)}")
    else:
        print("No discount you will pay bill {bill}")
elif day.lower() in ["saturday","sunday"]:
    print(f"Your bill is {bill-(bill*0.15)}")
else:
    print("invalid day")

# 88. Shape Identifier: Design a program that takes two inputs (length1,length2) and identifies the geometric shape based on the values:
# If lengths are equal: Square
# If one length is twice the other: Rectangle
# Otherwise: Not a square or rectangle

len1 = float(input("Enter length1: "))
len2 = float(input("Enter length2: "))
if len1 == len2:
    print("Square")
elif len2**2 == len1 or len1**1 == len2:
    print("Rectangle")
else:
    print("Not a square or rectangle!!")
    
# 89. WAP to check the type of a triangle (Equilateral,isosceles,scalene)
# using nested -if

side1 = float(input("Enter a Side(cm): "))
side2 = float(input("Enter a side2(cm): "))
side3 = float(input("Enter a side3(cm): "))
if side1+side2>side3 and side3+side1>side2 and side2+side3>side1:
    if side1==side2==side3:
        print("Equi Triangle")
    else:
        if side1 == side2 or side2 == side3 or side1 == side3:
            print("Isoceles Triangle")
        else:
            print("Scalene Traingle")
else:
    print("Invalid Triangle")

# 90. Wap to accept any number from 1 to 5 and display that number in word form. if they enter more than 5 then print no match.

num = int(input("Enter a Number(1 t0 5): "))
if 1<=num<=5:
    if num==1:
        print("One")
    elif num==2:
        print("Two")
    elif num==3:
        print("Three")
    elif num==4:
        print("Four")
    else:
        print("Five")
else:
    print("No Matched")

# 91. Wap to take input as only collections.

# i) if the type of input is a list then ask the value from the user and insert it in the middle index of that list. and print that list.
# ii) if type of input is tuple print 'cannot append tuple is immutable'
# iii)if type is set, take the input from the user. if the value is immutable then only add it to the set and print the set otherwise print 'enter only
# immutable collection'
# iv) if type of input is dictionary take key and value as user input and add the key and value pair using syntax to add key value . and print the dictionary.

collection = eval(input("Enter any collection: "))
if type(collection) == list:
    value = input("Enter value: ")
    middle_index = len(collection)//2
    collection.insert(middle_index,value)
    print(collection)
elif type(collection) == tuple:
    print("Cannont append tuple is immutable")
elif type(collection) == set:
    value = eval(input("Enter data: "))
    if type(value) not in [set,list,dict]:
        collection.add(value)
        print(collection)
    else:
        print("Enter Only Immutable collection")
elif type(collection) == dict:
    key = eval(input("Enter key: "))
    value = eval(input("Enter value: "))
    collection[key] = value
    print(collection)
else:
    print("single value datatype or string")        