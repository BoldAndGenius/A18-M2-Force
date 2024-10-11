# 85. Write a program.To check the type of a given character.

character = input("Enter any character : ")
if 'a'<=character<='z' or 'A'<= character<= "Z":
    print("Alphabets")
elif '0'<character<='9':
    print("Digits.")
else:
    print("Special Characters")
    
    
 
# Question No. 86   
# Write a program to consider an integer number. Print happy if the number is divisible by two. Print SAD if the number is divisible by 5 and print square of the numbers only if it is divisible by seven else print the number as it is.


number = int(input('Enter any number : '))
if number%2 == 0:
    print("Happy.")
if number%5==0:
    print("Sad.")
if number%7==0:
    print(number*number)
else:
    print(number)
    
    
    
    
# Question No. 88
# Program to consider an input string. Print the string as it is if it is palindrome. Print the reverse string if it has an even number of characters. Print all the characters present at an odd index if the string is having an odd number of characters.

input_string = 'kiran'
reversed = input_string[::-1]
if input_string == reversed:
    print(input_string)
if len(input_string)%2==0:
    print(reversed)
else:
    print(input_string[: :2])





# Question No. 91
# 91. Write a program to print the length of given data only if it is even.

data = input("Enter any data : ")  # 'kiran', '12', list,string
length = len(data)
if length%2 == 0:
    print(length)
else:
    print("Invalid")
    
    
    
# Question No. 93
#  Write a program.To check second greatest among three numbers using nested if.

num1 = int(input("Enter a first number : "))  # 2
num2 = int(input("Enter the second number : "))  # 6
num3 = int(input("Enter the third number : "))  # 4  

if num1>num2:
    if num1>num3:
        print(num2, "is 2nd Greatest.")
    else:
        print(num1, "is 2nd Greatest.")
else:
    if num2>num3:
        print(num1, "is 2nd greatest.")
    else:
        print(num2,"is 2nd greatest.")
        
        
# The logic is, 
# first check, if num1>num2, True, it means, num1 is greatest, then check for num1>num3 or not...if yes, then num2 is the 2nd greatest.
# else num1 will be 2nd greatest.
# if num1 is not > num2: ...it means, num2 is greatest, then check with num3, is num2>num3, if yes.....num1 is 2nd greatest. or else num2 is 2nd greatest. 







# Question No. 94 
# Write a program that determines the movie ticket price based on the age and day of the week Adults (18+): $12 (except for Tuesdays: $10) Children (under 18): $8 (except for Tuesdays: $6) Seniors (65+): $8 (always)


age = int(input("Enter an age : "))
day = input("Enter a day : ").lower()
tiket_price = 0
if 18<age<65 and day != "tuesday":
    ticket = 12
elif 18<age<65 and day == "tuesday" :
    ticket = 10
elif age<18 and day!= 'tuesday':
    ticket = 8
elif age<18 and day == 'tuesday':
    ticket = 6
elif age>65:
    ticket = 8 
print("Your Movie Ticket Price is :",ticket," $")







# Question - 95
# Leap Year Checker: Write a program that determines if a given year is a leap year. A leap year is a year divisible by 4, but not by 100 unless it's also divisible by 400.


# leap year - exactly divisible by 4, except for century year. 
# century year only be leap year, if it is only divisible by 400. 


# 2024 -- It is fully divisible by 4 -- therefore it is leap year.
# 2100  --- It is fully divisible by 4, but it is not a leap year. Since, it is a century year (fully divisible by 100), then we have to check whether this year is divisible by 400 or not. 


given_year = int(input("Enter an year: "))
if given_year%4 == 0:
    if given_year%100 == 0:  # check the year is century or not
        if given_year%400 == 0: # if century year, it should be divisible by 400, then leap year
            print("Leap Year.")
        else:  # century year is not divisible by 400, not a leap year
            print("Not a Leap Year.")
    else:  # not a century year, but it is divisible by 4..therefore leap year
        print("Leap Year.")
else:  # not divisible by 4, therefore not a leap year
    print("Not a Leap Year.")
    
    
    
# logic - 
# if year is divisible by 4, it can be a leap year, it not divisible it is not a leap year. 
# now check if it is divisble by 4, not check for century year, if it is divisble by 100, it means it is a cetury year, now check is it divisible by 400, if yes ...then it is a leap year. 


    


