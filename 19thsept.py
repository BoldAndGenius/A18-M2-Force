# Simple If 

# Question - 11 
# Write a program To register for a company only if job location is Bangalore.

job_location = input("Enter the Job Location :").lower()
if job_location == "bangalore":
    print("You are eligible for registration.")
    

# Question - 12 
# Write a program to check whether the given number is even.
number = int(input("Enter a number :"))
if number % 2 == 0:
    print("The number is even.")
    
    
# Question - 13 
# Write a program to check whether the given number is odd.
number = int(input("Enter a number :"))
if number % 2 != 0:
    print("The number is Odd.")

# Question - 14 
# Write a program to check whether the given number lies between 5 to 10.
number = int(input("Enter a number :"))
if 5 <= number <= 10:
    print("The given number lies in between 5 to 10 ")


# Question - 15 
# Write a program To check whether the given string is having more than three characters.

given_string = input("Enter a string :")
if len(given_string) > 3:
    print("Yes, the given string have more than 3 characters.")



# Question - 16 
# Write a program To check whether the given number is having 4 digits.

number = input("Enter a number :")
if len(number) == 4:
    print("The given number has 4 digits.")
    
    
# Question - 17 
# Write a program to check whether the given character is a vowel.

character = input("Enter a character :").lower()
if character in 'aeiou':
    print("The given character is vowel. ")
    


# Question - 18 
# Write a program to check whether the given integer number is even and multiple of five.

number = int(input("Enter a number :"))
if (number % 2 == 0)  and (number % 5 == 0):
    print("The given number is even & multiple of 5 ")
    
    
    
# Question - 19
# Write a program to check whether the given string is character...means the lenght is 1
given_string = input("Enter a string :")
if len(given_string) == 1:
    print("The given string is a character.")
    

# Question - 20
# Write a program to check whether the given character is uppercase alphabet.

given_character = input("Enter a character :")
if given_character.isupper():
    print("The given character is a Uppercase Alphabet.")
    
    

