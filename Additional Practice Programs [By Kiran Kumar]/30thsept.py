# Collection is Homogenous or Not

collection = eval(input("Enter a Collection : "))  # [1,2]  # {1,2}
homogenous = True
# logic is  -- compare the data type of all elements from the data type of 1st element
first_element = type(collection[0])
for item in collection:
    if type(item) != first_element:
        homogenous = False 
if homogenous == True:
    print("Homogenous Collection")
else:
    print("Heterogenous Collection")



# Given Number is Prime or Not 

number = int(input("Enter a Number : "))
if number == 1:
    print("Not a Prime Number, Please enter number greater than 1")
elif number == 2:
    print("Prime Number")
else:
    prime = True
    for num in range(2,number):
        if number % num == 0:
            prime = False
            break
    if prime == True:
        print("Number is Prime")
    else:
        print("Number is Not a Prime")



# Validate Username & Password using For Loop & While Loop

actual_username = "kiran_kumar"
actual_password = "1234"

while True:
    username = input("Enter your Username : ")
    if username == actual_username:
        print("Right Username")
        break
for _ in range(3):
    password = input("Enter your Password : ")
    if password == actual_password:
        print("Login Successfully! ")
else:
    print("Tried 3 Times, So User is Blocked for 24 Hours")
    
    


# Check if the String consists only the Lower Character 

string = input("Enter any String :") #kIran
lowercase = True
for character in string:  #'k' #'I'
    if character.isupper():
        lowercase = False
        break
if lowercase == True:
    print("String consists only the Lower Characters")
else:
    print("String not consists only the Lower Characters")
    
    
    
# Print n natural numbers using While Loop

# natural number means, it starts from 1 and it will go to n
start = 1  # initialization
end = int(input("Enter till what number you want to print the natural numbers :"))
while start <= end:  #condition
    print(start)
    start = start + 1 # updation
    

# Print n natural numbers using For Loop
start = 1
end = int(input("Enter till what number you want to print the natural numbers :"))
for number in range(start,end+1,1):
    print(number)
    
    
# All even numbers from 0 to 100 using For Loop
for num in range(0,101,2):
    print(num)
    
# All Even Numbers from 0 to 100 using While Loop
start = 0
end = 100
while start <= 100:
    if start % 2 == 0:
        print(start)
    start = start + 1
    
    

# Multiplication Table Using For Loop

num = int(input("Enter a number for which you want to print the table : "))
for i in range(1,11):
    print(num*i)


# Multiplication Table Using While Loop
start = 1
end = 10
num = int(input("Enter a number for which you want to print the table :"))
while start <= end:
    print(num*start)
    start = start + 1
    
    
# Odd Numbers from 0 to 100 using For Loop
for num in range(1,100,2):
    print(num)
    
# Odd Numbers from 0 to 100 using While Loop
start = 1
end = 100
while start <= end:
    print(start)
    start = start + 2
    
    
# Odd Numbers from 0 to 100 in Reverse Order using For Loop
for num in range(99,0,-2):
    print(num)
    

# Odd Numbers from 0 to 100 in Reverse Order using While Loop
start = 99
end = 1
while start>=end:
    print(start)
    start = start - 2
    

# Factorial of a Given Number Using For Loop

num = int(input("Enter a number for which you want to find the factorial :"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print("The factorial of a number is ",factorial)


# Factorial of Number Using While Loop

start = 1
num = int(input("Enter a number for which you want to find the factorial :"))
factorial = 1
while start <= num:
    factorial = factorial * start
    start = start + 1
    
print("The factorial of a number is ",factorial)



# Fibonacci Series Using For Loop & Swappig Concept

num1 = 0
print(num1)
num2 = 1
print(num2)

number = int(input("Enter number at which you want to print the series :"))
for _ in range(0,number-2):
    num3 = num1 + num2   # num3 = 0+1 = 1
    print(num3)
    #swapping
    num1 = num2
    num2 = num3


# Fibonacci Series Using List 

series = [0,1]
num  = int(input("Enter number at which you want to print the Series : "))
if num == 1:
    print(f"[{series[0]}]")
elif num == 2:
    print(f"[{series[0]}, {series[1]}]")
elif num>2:
    for _ in range(num-2):
        third_digit = series[-1] + series[-2]
        series.append(third_digit)
    print(series)
else:
    print("Invalid Number (Number should be greater than 0)")
