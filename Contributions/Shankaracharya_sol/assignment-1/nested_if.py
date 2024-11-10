#Write a program to create an Instagram login page.
login_username = {"shanky" : "shanky@612","satya" : "satya@72011" ,"divya" : "divya@82001" ,"susmna" : "cutipie1997@"}
login_email = {"shankyrai612@gmail.com" : "shanky@612","satyarai007@gmail.com" : "satya@72011" ,"divyanidhisingh0012@gmail.com" : "divya@82001" ,"susmnarai1997@gmail.com" : "cutipie1997@"}
login_phone_number = {"6394399793" : "shanky@612","8081943453" : "satya@72011" ,"8840338328" : "divya@82001" ,"8081962502" : "cutipie1997@"}

print("          Welcome to Instagram Login page          ")

username = input("Enter your username:")
password = input("Enter your password:")

if username in login_username:
    actual_password = login_username[username]
    
    if actual_password == password:
        print("you have successfully logged in")
    else:
        print("wrong password")
        
        password = input("Enter your password again:")
        if actual_password == password:
            print("you have successfully logged in")
            
elif username not in login_username:
    print("wrong username try with your email id")
    email = input("Enter your email:")
    
    if email in login_email:
        actual_password = login_email[email]
        
        if actual_password == password:
            print("you have successfully logged in")
        else:
            print("wrong password")
            
            password = input("Enter your password again:")
            if actual_password == password:
                print("you have successfully logged in")
                
    elif email not in login_email:
        print("wrong email id try with your number")
        phone_number = input("Enter your phone number:")
        
        if  phone_number in login_phone_number:
            actual_password = login_phone_number[phone_number]
            if actual_password == password:
                print("you have successfully logged in")
            else:
                print("wrong password")
            
                password = input("Enter your password again:")
                if actual_password == password:
                    print("you have successfully logged in")
        else:
            print("User does not exist please sign up")

#Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3.
heterogeneous_tuple = ( 1,5.0,['hello sir'],"hello",{10,20,30})
if len(heterogeneous_tuple) % 2 == 1:
    middle_value = heterogeneous_tuple[len(heterogeneous_tuple)//2]
    if type(middle_value) == str:
        if len(middle_value) > 3:
            print(f"The middle value of the tuple is:{middle_value}")
        else:
            print("length of middle is less than or equal to 3")
    else:
        print("middle value is not a string")
else:
    print("tuple has no middle value")
    
#Write a program.To check the greater among four numbers using nested if.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
num3 = float(input("Enter num3:"))
num4 = float(input("Enter num4:"))
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("num1 is greater")
        else:
            print("num4 is greater")
    else:
        print("num3 is greater")
else:
    if num2 > num3:
        if num2 > num4:
            print("num2 is greater")
        else:
            print("num4 is greater")
    else:
        print("num3 is greater")

#Write a program to find the second greatest among four numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            greatest = num1
        else:
            greatest = num4
    elif num3 > num4:
        greatest = num3
    else:
        greatest = num4
else:
    if num2 > num3:
        if num2 > num4:
            greatest = num2
        else:
            greatest = num4
    elif num3 > num4:
        greatest = num3
    else:
        greatest = num4

################################ Now find the second greatest by checking numbers other than the greatest  ################################################
if greatest == num1:
    if num2 > num3 and num2 > num4:
        second_greatest = num2
    elif num3 > num4:
        second_greatest = num3
    else:
        second_greatest = num4
elif greatest == num2:
    if num1 > num3 and num1 > num4:
        second_greatest = num1
    elif num3 > num4:
        second_greatest = num3
    else:
        second_greatest = num4
elif greatest == num3:
    if num1 > num2 and num1 > num4:
        second_greatest = num1
    elif num2 > num4:
        second_greatest = num2
    else:
        second_greatest = num4
else:
    if num1 > num2 and num1 > num3:
        second_greatest = num1
    elif num2 > num3:
        second_greatest = num2
    else:
        second_greatest = num3
        
print(f"The second greatest number is: {second_greatest}")

#Write a program To check the type of a given character.
character = input("Enter any character:")
if character.isupper():
    print("character is uppercase")
else:
    if character.islower():
        print("character is lowercase")
    else:
        if character.isnumeric():
            print("character is numeric")
        else:
            print("character is special char")
            
#Write a program to consider an integer number. Print happy if the number is divisible by two. Print SAD if the number is divisible by 5 and print square of the numbers only if it is divisible by seven else print the number as it is.
num = int(input("Enter an integer:"))
if num % 2 == 0:
    print("HAPPY")
else:
    if num % 5 == 0:
        print("SAD")
    else:
        if num % 7 == 0:
            print(f"square of {num} is:{num**2}")
        else:
            print(num)
            
#Write a program to find the smallest among three numbers.
num1 = eval(input("Enter num1:"))
num2 = eval(input("Enter num2:"))
num3 = eval(input("Enter num3:"))

if num1 < num2:
    if num1 < num3:
        print("num1 is smaller")
    else:
        print("num3 is smaller")
else:
    if num2 < num3:
        print("num2 is smaller")
    else:
        print("num3 is smaller")
        
#Program to consider an input string. Print the string as it is if it is palindrome. Print the reverse string if it has an even number of characters. Print all the characters present at an odd index if the string is having an odd number of characters.
string = input("Enter a string:")
reverse_string = string[::-1]
if reverse_string == string:
    print(string)
else:
    if len(string) % 2 ==0:
        print(reverse_string)
    else:
        odd_index = {string[1],string[3],string[5]}
        print(odd_index)

#Write a program to print middle Character.Given string only if it is upper case character.
string = input("Enter a string:")
if string.isupper():
    
    if len(string) % 2 == 0:
        length = len(string) // 2
        middle_char = [string[length-1],string[length]]
        print(f"at {length-1} and {length} index positions middle characters are {middle_char}")
    else:
        length = len(string) // 2
        middle_char = string[length]
        print(f"at {length} index position middle character is {middle_char}")
else:
    print("string is not uppercase")
    
#Write a program to check whether a given character is vowel or consonant using nested if.
character = input("Enter any character:")
if character.isalpha():
    if character in 'aeiouAEIOU':
        print("it's vowel")
    else:
        print("It's consonent")
else:
    print("Character is not an alphabet")
    
#Write a program to print the length of given data only if it is even.
data = eval(input("Enter data:"))
if len(data) % 2 == 0:
    print(len(data))
else:
    print("Length of given data is not even")
    
#Write a program to check greatest among three numbers using nested if.
num1 = eval(input("Enter num1:"))
num2 = eval(input("Enter num2:"))
num3 = eval(input("Enter num3:"))

if num1 > num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")
else:
    if num2 > num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")
        
#Write a program.To check second greatest among three numbers using nested if.
num1 = eval(input("Enter num1:"))
num2 = eval(input("Enter num2:"))
num3 = eval(input("Enter num3:"))

if num1 > num2:
    if num1 > num3:
        print("num3 is 2nd greatest")
    else:
        print("num1 is 2nd greatest")
else:
    if num2 > num3:
        print("num3 is 2nd greatest")
    else:
        print("num2 is 2nd greatest")
        
#Write a program that determines the movie ticket price based on the age and day of the week
# Adults (18+): $12 (except for Tuesdays: $10)
# Children (under 18): $8 (except for Tuesdays: $6)
# Seniors (65+): $8 (always)
age = int(input("Enter your age:"))
if 18 < age <= 65:
    day_of_week = input("Enter day of week:")
    if day_of_week != 'tuesday':
        ticket_price_adults = f"$12"
        print(f"The movie ticket price for age {age} is {ticket_price_adults}")
    else:
        ticket_price_adults = f"$10"
        print(f"The movie ticket price for age {age} is {ticket_price_adults}")
elif age <= 18:
    day_of_week = input("Enter day of week:")
    if day_of_week != 'tuesday':
        ticket_price_children =f"$8"
        print(f"The movie ticket price for age {age} is {ticket_price_children}")
    else:
        ticket_price_children =f"$6"
        print(f"The movie ticket price for age {age} is {ticket_price_children}")
else:
    ticket_price_seniors = f"$8"
    print(f"The movie ticket price for age {age} is {ticket_price_seniors}")

#Leap Year Checker: Write a program that determines if a given year is a leap year. A leap year is a year divisible by 4, but not by 100 unless it's also divisible by 400.
#Vending Machine: Create a program for a vending machine that takes product code (integer) and amount paid (float) as input. It should check the product price (stored in a dictionary) and dispense the product if enough is paid. Use nested ifs for different error messages (e.g., invalid code, insufficient funds).
product_code = int(input("Enter product code:"))
product_credentials = {100:127.5,200:189.87}

if product_code in product_credentials:
    paid_amount = float(input("Enter paid amount:"))
    product_price = product_credentials[product_code]
    if paid_amount >= product_price:
        print(f"Dispence the product code:{product_code}")
    else:
        print("insufficient funds")
else:
    print("invalid code")
    
#Restaurant Discount: Write a program that calculates a restaurant bill with a discount based on the day of the week and party size:
#Weekdays (Mon-Fri), party < 4: No discount.
#Weekdays (Mon-Fri), party >= 4: 10% discount.
#Weekends (Sat-Sun), any party size: 15% discount.
bill = float(input("Enter the bill:"))
day = input("Enter day of the week:")

if day in ['Mon','Tue','Wed','Thu','Fri'] :
    party_size = int(input("Enter the party size:"))
    if party_size < 4:
        print("No discount")
        print(bill)
    else:
        bill -= (10/100) * bill
        print(bill)
else:
    bill -= (15/100) * bill
    print(bill)

#Shape Identifier: Design a program that takes two inputs (length1, length2) and identifies the geometric shape based on the values:
#If lengths are equal: Square
#If one length is twice the other: Rectangle
#Otherwise: Not a square or rectangle.
length1 = float(input("Enter length1:"))
length2 = float(input("Enter length2:"))

if length1 == length2:
    print("Square")
else:
    if length1 == (2 * length2) or length2 == (2 * length1):
        print("Rectangle")
    else:
        print("Not a Square or Rectangle")
        
#WAP to check the type of a triangle (Equilateral,isosceles,scalene) using nested -if
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
        
#Wap to accept any number from 1 to 5 and display that number in word form. if they enter more than 5 then print no match.
num = int(input("Enter number from 1 to 5:"))
if 1 <= num <= 5:
    if num == 1:
        print("One")
    elif num == 2:
        print("Two")
    elif num == 3:
        print("Three")
    elif num == 4:
        print("Four")
    else:
        print("Five")
else:
    print("No Match")

#Wap to take input as only collections. 
#i) if the type of input is a list then  ask the value from the user and insert it in the middle index of that list. and print that list.
#	ii) if type of input is tuple print 'cannot append tuple is immutable'
#	iii)if type is set, take the input from the user. if the value is immutable then only add it to the set and print the set otherwise print 'enter only immutable collection'
#	iv) if type of input is dictionary take key and value as user input and add the key and value 	pair using syntax to add key value . and print the dictionary.
collection = eval(input("Enter a collection:"))

if type(collection) is list:
    value = eval(input("Enter a value:"))
    middle_index = len(collection) // 2
    if len(collection) % 2 == 0:
        collection.insert(middle_index,value)
        print(collection)
    else:
        collection.insert(middle_index+1,value)
        print(collection)
        
elif type(collection) is tuple:
    print('cannot append tuple is immutable')
    
elif type(collection) is set:
    value = eval(input("Enter a value:"))
    if type(value) in [int,float,complex,str,tuple]:
        collection.add(value)
        print(collection)
    else:
        print('enter only immutable collection')
        
elif type(collection) is dict:
        key = input("Enter anything which is of immutable data type:")
        value =input("Enter value:")
        collection[key] = value
        print(collection)
