#M.Anil Kumar

'''48.Write a program to check the relation between two integer numbers'''
num1=int(input('Enter number1:'))
num2=int(input('Enter number2:'))
if num1>num2:
    print('num1 is greater than num2')
elif num1<num2:
    print('num1 is less than num2')
else:
    print('num1 equal to num2')


'''49.Write a program to check whether a given character is uppercase or lowercase or number. 
If character is uppercase print uppercase, If character is lowercase print lowercase. 
If the character is a number, print the ascii number of it. 
'''
char=input('Enter a character:')
if char.isupper():
    print('Uppercase')
elif char.islower():
    print('Lowercase')
elif char.isnumeric():
    ascii=ord(char)
    print(f'The ascii number of {char} is : {ascii}')

'''50.Write a program to check whether a given character is a vowel or consonant. 
If a given character is a vowel, store the character inside the list.
 If a given character is consonant, display the ASCII value of that character. 
'''
char=input('Enter a character:')
list1=[]
if char in 'aeiouAEIOU':
    list1.append(char)
    print(list1)
elif char.isalpha():
    print(f'The ascii number of {char} is : {ord(char)}')


'''51.Write a program to check if the given data is individual data type or not.'''
data=eval(input('Enter a data:'))
if type(data) in [int,float,bool,complex]:
    print('Indiviual datatype')
elif type(data) in [str,list,tuple,set,dict]:
    print('Not individual datatype')


'''52.write a program to check whether the given integer single digit or two digits or three digits or more than three digits
'''
num=int(input('Enter a number:'))
if -9<=num<=9:
    print('Single digit')
elif -99<=num<=99:
    print('Two digits')
elif -999<=num<=999:
    print('Three digits')
else:
    print('More than three digits')


''''53.write a program to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5'''
num=int(input('Enter a number:'))
if num%3==0 and num%5==0:
    print('Fizzbuzz')
elif num%3==0:
    print('buzz')
elif num%5==0:
    print('Fizz')


'''54.Write a program to predict grade of the student based on the obtained result 
'''
result=int(input('Enter result:'))
if 90<=result<=100:
    print('Grade A+')
elif 80<=result<=89:
    print('Grade A')
elif 70<=result<=79:
    print('Grade B')
elif 60<=result<=69:
    print('Grade C')
elif 50<=result<=59:
    print('Grade D')
elif 40<=result<=49:
    print('Grade E')
elif result<40:
    print('Grade F')
else:
    print('Invalid Marks')


'''55.Write a program to check whether the entered character is uppercase or lowercase or number or special character
'''
char=input('Enter a character:')
if char.isupper():
    print('Uppercase')
elif char.islower():
    print('Lowercase')
elif char.isnumeric():
    print('Number')
else:
    print('Special character')

'''56.Write a program to find the greatest among two numbers'''
num1=input('Enter number1:')
num2=input('Enter number2:')
if num1>num2:
    print('num1 is greater')
elif num2>num1:
    print('num2 is greater')
else:
    print('Both are equal')

'''57.Write a program to find the smallest among three numbers '''
num1=int(input('Enter number1:'))
num2=int(input('Enter number2:'))
num3=int(input('Enter number3:'))
if num1<num2 and num1<num3:
    print('num1 is smallest')
elif num2<num1 and num2<num3:
    print('num2 is smallest')
else: 
    print('num3 is smallest')

'''58.Write a program to find the greatest among four numbers'''
num1=int(input('Enter number1:'))
num2=int(input('Enter number2:'))
num3=int(input('Enter number3:'))
num4=int(input('Enter number4:'))
if num1>num2 and num1>num3 and num1>num4:
    print('num1 is greatest')
elif num2>num1 and num2>num2 and num2>num4:
    print('num2 is greatest')
elif num3>num1 and num3>num2 and num3>num4:
    print('num3 is greatest')
else:
    print('num4 is greatest')


'''59.Write a program to find the smallest among four numbers'''
num1=int(input('Enter number1:'))
num2=int(input('Enter number2:'))
num3=int(input('Enter number3:'))
num4=int(input('Enter number4:'))
if num1<num2 and num1<num3 and num1<num4:
    print('num1 is smallest')
elif num2<num1 and num2<num2 and num2<num4:
    print('num2 is smallest')
elif num3<num1 and num3<num2 and num3<num4:
    print('num3 is smallest')
else:
    print('num4 is smallest')


'''60.Write a program to calculate the electricity bill.According to the following criteria, 
for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, 
the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000'''
units=int(input('Enter number of units:'))
bill=0
if units<100:
    bill=0
elif 100<units<=200:
    bill=(units-100)*5
elif units>200:
    bill=(100*5)+(units-100)*10
print(f'Current Bill is:{bill}')

'''61.Write a program to accept percentages from the user and display the grade according to the following criteria. 
If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, gra inde is B if marks is greater than or equal to 60,
 and less than equals to 80 grade is C, else if it is less than 60 grade is D'''
percentage=float(input('Enter percentage:'))
if percentage>90:
    print('Grade is A')
elif 80<percentage<90:
    print('Grade is B')
elif 60<=percentage<=80:
    print('Grade is C')
elif percentage<60:
    print('Grade is D')

'''62.Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria 
if cost price is greater than One Lac.The tax is 50%, if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% 
and if it is less than equals to 50,000 the tax is 5%.
'''
cost_price=float(input('Enter cost price of bike:'))
if cost_price>100000:
    tax=cost_price*0.5
    print(f'Road tax: {tax}')
elif 50000<cost_price<=100000:
    tax=cost_price*0.1
    print(f'Road tax: {tax}')
elif cost_price<=50000:
    tax=cost_price*0.05
    print(f'Road tax: {tax}')

'''63.Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.
'''
day=int(input('Enter day number:'))
if day==1:
    print('Sunday')
elif day==2:
    print('Monday')
elif day==3:
    print('Tuesday')
elif day==4:
    print('Wednesday')
elif day==5:
    print('Thursday')
elif day==6:
    print('Friday')
elif day==7:
    print('Saturday')

'''64.Write a program to accept a number from 1 to 12 and display name of the month and days in that month like one for January and number of days is 31 and so on.
'''
month=int(input('Enter month number:'))
if month==1:
    print('January,number of days is 31')
elif month==2:
    print('February,number of days is 28')
elif month==3:
    print('March,number of days is 31')
elif month==4:
    print('April,number of days is 30')
elif month==5:
    print('May,number of days is 31')
elif month==6:
    print('June,number of days is 30')
elif month==7:
    print('July,number of days is 31')
elif month==8:
    print('August,number of days is 31')
elif month==9:
    print('September,number of days is 30')
elif month==10:
    print('October,number of days is 31')
elif month==11:
    print('November,number of days is 30')
elif month==12:
    print('December,number of days is 31')


'''65.Accept any city from the user and display monuments of that city. 
For Delhi it is Red Fort, Agra- Taj Mahal, Jaipur- Jal Mahal.
'''
city=input('Enter city name:')
if city=='Delhi':
    print('Red Fort')
elif city=='Agra':
    print('Taj Mahal')
elif city=='Jaipur':
    print('Jal Mahal')


'''66.Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
'''
side1=int(input('Enter first side of triangle:'))
side2=int(input('Enter second side of triangle:'))
side3=int(input('Enter third side of triangle:'))
if side1==side2==side3:
    print('Equilateral triangle')
elif side1==side2 or side2==side3 or side3==side1:
    print('Isosceles triangle')
else:
    print('Scalene triangle')


'''67.Accept the number of days from the user and calculate the charge of library according to the following criteria. 
Till five days it is ₹2 per day, 6 to 10 days it is ₹3 per day, 11 to 15 days it is ₹4.00 per day and after 15 days it is five Rupees per day.
'''
days=int(input('Enter number of days:'))
if days<=5:
    charge=days*2
    print(f'Library charge is: ₹{charge}')
elif 6<=days<=10:
    charge=5*2+(days-5)*3
    print(f'Library charge is: ₹{charge}')
elif 11<=days<=15:
    charge=(5*2)+(5*3)+(days-10)*4
    print(f'Library charge is: ₹{charge}')
else:
    charge=(5*2)+(5*3)+(5*4)+(days-15)*5
    print(f'Library charge is: ₹{charge}')


'''68.Accept the kilometers covered and calculate the bill according to the following criteria. 
For 1st 10 kilometers it is ₹11.00 per kilometer, For next 90 kilometers it is rupees 10 per kilometer 
and after that it is ₹9 per kilometer. 
'''
kilometers=int(input('Enter the kilometers covered:'))
if kilometers<=10:
    bill=11*kilometers
    print(f'Bill:{bill}')
elif 10<kilometers<=100:
    bill=(10*11)+(kilometers-10)*10
    print(f'Bill:{bill}')
else:
    bill=(10*11)+(90*10)+(kilometers-100)*9
    print(f'Bill:{bill}')


'''69.WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.
'''
choice=int(input('Enter your choice(1:celsius to kelvin conversion, 2:kelvin to celsuis conversion):'))
if choice==1:
    celsius=float(input('Enter temperature in celsius:'))
    kelvin=celsius+273.15
    print(f'Temperature in kelvin is: {kelvin}K')
elif choice==2:
    kelvin=float(input('Enter temperature in kelvin:'))
    celsius=kelvin-273.15
    print(f'Temperature in celsius is: {celsius}°C')
