# Define a Function which adds two number 

def add():
    num1 = int(input("Enter the number 1 : "))
    num2 = int(input("Enter the number 2 : "))
    print(f"The sum of {num1} and {num2} is {num1+num2}")
    
    
    
# Define a Function which asks for a Username & Password and print it.
def user_credentials():
    username = input("Enter your Username : ")
    password = input("Enter your Password : ")
    print(f"Your Username is {username} and Your Password is {password}")
    
    
# Define a Function which returns the square of a number if it is even else cube of it.
def get_square_or_cube():
    num = int(input("Enter any Number : "))
    if num % 2 == 0:
        return num ** 2
    else:
        return num ** 3