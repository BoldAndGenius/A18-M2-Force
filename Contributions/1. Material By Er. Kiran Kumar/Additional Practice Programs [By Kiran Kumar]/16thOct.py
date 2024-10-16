
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