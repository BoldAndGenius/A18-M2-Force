
# Function to Check a Given String is Palindrome or Not
def palindrome_checker(string):
    reverse = string[::-1]
    if string == reverse:
        return "Palindrome"
    else:
        return "Not a Palindrome"
check = palindrome_checker("mam")
print(check)



# Function to check a Given Number is Odd or Even

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
check = check_odd_even(5)
print(check)


# Function to return sum of two numbers 

def sum_two_num(num1,num2):
    return num1 + num2 
sum = sum_two_num(10,20)
print(sum)



# Function to return Substraction of Two Numbers 

def subtract_two_num(num1,num2):
    return num1 - num2 
subtract = subtract_two_num(20,5)
print(subtract)



# Function to return Multiplication of Two Numbers
def multiplication_two_num(num1,num2):
    return num1 * num2 
multiplication = multiplication_two_num(20,30)
print(multiplication)



# Function to return Division of Two Numbers
def division_two_num(num1,num2):
    return num1 / num2 
division = division_two_num(10,4)
print(division)


# Function to return Remainder of Two Numbers
def remainder_two_num(num1,num2):
    return num1 % num2 
remainder = remainder_two_num(20,6)
print(remainder)


# Function to return Square of a Number
def square_of_num(num):
    return num ** 2 
square = square_of_num(10)
print(square)


# Function to return Cube of a Number
def cube_of_num(num):
    return num ** 3
cube = cube_of_num(15)
print(cube)


# Function - A block of reusable code. 
# place () after the function name to invoke it. 

# Method - 1
def happy_birthday(p1,p2):
    print(f"Happy Birthday {p1}")
    print(f"You are {p2} years old.")

name = input("Enter you name : ")
age = int(input("Enter you age : "))
happy_birthday(name,age)

# Method - 2

def happy_birthday(p1,p2):
    return f"Happy Birthday {name}. \nNow you are {age} years old"
    
name = input("Enter you name : ")
age = int(input("Enter your age : "))
wish = happy_birthday(name,age)
print(wish)