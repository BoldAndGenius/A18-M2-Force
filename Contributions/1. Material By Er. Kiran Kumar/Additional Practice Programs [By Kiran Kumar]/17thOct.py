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
    
    

# Define a Function which returns the last element of the Collection 
def last_element():
    collection = eval(input("Enter any collection : "))
    return collection[-1]



# Define a Function which displays the multiplication table of a number. 
def display_table(num):
    for factor in range(1,11):
        print(f"{num} X {factor} = {num*factor}")



# Define a Function which displays all the vowels in a given string
def display_vowel(string):
    vowel = ""
    for char in string:
        if char in "aeiouAEIOU":
            vowel = vowel + char  
    print(vowel)
display_vowel("kiran")



# Define a Function which returns all the keys from the dictionary that are string.
def get_key(dictionary):
    keys = []
    for key in dictionary:
        if type(key) == str:
            keys.append(key)
    print(keys)
# get_key({"name": "kiran", "age":18, "address": "Bangalore", 32 : 45})
            
