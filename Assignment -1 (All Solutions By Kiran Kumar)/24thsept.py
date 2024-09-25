# Question - 71 
# Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit, and after 200 units, the price is rupees 10 per unit. If the input is 350 then total bill amount is Rupees 2000.

# calculate electricity bill
# 0 to 100 Units = No Charge.
# 100 to 200 Units = 5 Rs Per Unit.
# 200 +  = 10 Rs Per Unit.

# demo example - Need to validate
# input is = 350 Unit
# Bill Amount = 2000 Rs 

# (Good Question to Practice) - A Practical example of if elif statements.

units = float(input("Enter Number of Units : "))
if 0 <= units < 100:
    print("No Charges") 
elif 100 <= units < 200:
    print(f"Total Bill = {(units-100)*5}")
elif units >= 200:
    print(f"Total Bill = {(100 * 5)+ ((units-200)*10)}  ")
    # unit = 250,   0 to 100 - no, 100 to 200 = 100*5 ,  200 to 250 = 50*10
    
    










# Question - 72 
#Write a program to accept marks from the user and display the grade according to the following criteria. If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, then grade is B if marks is greater than or equal to 60, and less than equals to 80 grade is C, else if it is less than 60 grade is D



# marks > 90    - A Grade
# marks > 80  and marks < 90    - B Grade
# marks >= 60  and marks <= 80    - C Grade
# marks < 60     -  D Grade


marks = float(input("Enter a Percentage :"))
if  marks > 90:
    print("Grade is A")
elif 80 < marks < 90:
    print("Grade is B")
elif 60 <= marks <= 80:
    print("C Grade")
elif marks < 60:
    print("D Grade")
else:
    print("Invalid")
    
    







# Question - 73
# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria if cost price is greater than One Lac.The tax is 50%, if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% and if it is less than equals to 50,000 the tax is 5%


cost_price = float(input("Enter a Cost Price"))  # 50000

if cost_price > 100000:
    # 50% tax
    road_tax = (cost_price*50) / 100
    print(road_tax)
    
elif 50000 < cost_price <= 100000:
    # tax is 10%
    road_tax = (cost_price*10)/100
    print(road_tax)
    
elif cost_price <= 50000:
    # 5% tax
    road_tax = (cost_price*5)/100
    print(road_tax)









# Question - 74
# Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.

# 1 to 7
# Sunday, Monday, Tuesday, Wednesday 

'''

Match Case Syntax -

var = valu1
match var:
    case pattern1:
        case statement block
    case pattern2:
        case statement block
    case pattern3:
        case
    .
    .
    case _:
        Default Statement Block




Example -


option = input("""Enter the option from below :  \n 
            A - Pizza
            B - Burger
            C - Vadapav
            D - Golgappa""")
match option:
    case "A":    # case 1 :    (if integer)
        print("You have ordered Pizza")
    case "B":
        print("You have orderd Burger")
    case "C":
        print("You have ordered Vadapav")
    case "D":
        print("You have ordered Golgappa")
    case _ :  # by default (only be executed if not entered A, B, C)
        print("Invalid Option")



'''

# Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.

# 1 to 7
# Sunday, Monday, Tuesday, Wednesday 


number = input("""Enter number from 1 to 7 : \n
                   1 - Sunday
                   2 - Monday
                   3 - Tuesday
                   4 - Wednesday
                   5 - Thursday
                   6 - Friday
                   7 - Saturday
                   """)
match number:
    case '1':
        print("Sunday")
    case '2':
        print("Monday")
    case '3':
        print("Tuesday")
    case '4':
        print("Wednesday")
    case '5':
        print("Thursday")
    case '6':
        print("Friday")
    case '7':
        print("Saturday")
    case _:
        print("Invalid")
                   












# Question - 75
# Write a program to accept a number from 1 to 12 and display name of the month and days in that month like one for January and number of days is 31 and so on.


# we can easily use match case here.

number = input("""Enter a number between 1to 12 \n
               1 - January
               2 - February
               3 - March
               4 - April
               5 - May
               6 - June
               7 - July
               8 - August
               9 - September
               10 - October
               11 - November
               12 - December
                """)


match number:
    case '1':
        print("January, Total 31 Days")
    case '2':
        print("February, Total 28 Days")  # Assuming it's not a leap year, otherwise 28 or 29, We can use any
    case '3':
        print("March, Total 31 Days")
    case '4':
        print("April,Total 30 Days")
    case '5':
        print("May, Total 31 Days")
    case '6':
        print("June, Total 30 Days")
    case '7':
        print("July, Total 31 Days")
    case '8':
        print("August, Total 31 Days")
    case '9':
        print("September, Total 30 Days")
    case '10':
        print("October, Total 31 Days")
    case '11':
        print("November,Total 30 Days")
    case '12':
        print("December, Total 31 Days")
    case _:
        print("Invalid number")
        
        
        
        
        
        
        
    
    
    
    
# Question - 76
# Accept any city from the user and display monuments of that city. For Delhi it is Red Fort, Agra- Taj Mahal, Jaipur- Jal Mahal.



city = input("""Enter any city \n
             Delhi - Red Fort,
             Agra - Taj Mahal,
             Jaipur - Jal Mahal
             Bangalore - Bangalore Palace
             """)

match city:
    case 'Delhi':
        print("Red Fort")
    case "Agra":
        print("Taj Mahal")
    case "Jaipur":
        print("Bangalore Palace")
        
    # so on...we can add multiple cities with their respective monuments.
    case _:
        print("Invalid City")
        



# Question - 77
# Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.



side1 = float(input("Enter side 1 :"))
side2  = float(input("Enter Side 2 :"))
side3 = float(input("Enter Side 3 :"))

if side1 == side2 == side3:
    print("Equilateral Trianlge") # all three sides equal
# elif (side1 != side2) or (side1 != side3) or (side2 != side3): -- there is some bug in this logic
elif (side1 != side2 != side3):   
    print("Scalene Triangle") # no sides equal
else:
    print("Isosceles Triangle")  #two sides equal



# Question - 78
# Accept the number of days from the user and calculate the charge of library according to the following criteria. Till five days it is ₹2 per day, 6 to 10 days it is ₹3 per day, 11 to 15 days it is ₹4.00 per day and after 15 days it is five Rupees per day.



days = int(input("Enter number of days : "))
if days <= 5:
    library_charge = days*2
elif 6 <= days <= 10:
    library_charge = days*3
elif 11 <= days <= 15:
    library_charge = days*4
elif days > 15:
    library_charge = days*5
else:
    print("Invalid Days")
print(library_charge)
     









# Question - 79
# Accept the kilometers covered and calculate the bill according to the following criteria. For 1st 10 kilometers it is ₹11.00 per kilometer, For next 90 kilometers it is rupees 10 per kilometer and after that it is ₹9 per kilometer.

kilometer_covered = float(input("Enter How much Kilometers it covered : "))
if kilometer_covered<= 10:
    bill = kilometer_covered*11
elif 10 < kilometer_covered <= 100:    # 50 = >    10*11 + (50-10)*10  = 110 + 400 = 510
    bill = (10*11) + (kilometer_covered-10) * 10
elif kilometer_covered > 100:  # 110 =>   10*11 + 90*10 + (110 - 100) *9  = 110 + 900 + 90 = 1100
    bill =  (10*11) + (90*10) + (kilometer_covered -100 )* 9
else:
    print("Invalid")
print(bill)





# Question - 80
# WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.

# concept -
# Temperature at Kelvin = Teperature at Celsius + 273.15 
# Therefore, Temperature at Celsius = Temperature at Kelvin - 273.15

temperature = float(input("Enter a Temprature :"))
unit = input('Enter in which form you need to convert - ( "C" - Celsius,  "K" - Kelvin) ')

if unit == "K":
    # 50 K
    # kelvin to celsius
    celsius = temperature - 273.15
    print(celsius)
elif unit == "C":
    # 50 C
    # celsius to kelvin
    kelvin = temperature + 273.15
    print(kelvin)
else:
    print("Invalid Conversion")
    
    
