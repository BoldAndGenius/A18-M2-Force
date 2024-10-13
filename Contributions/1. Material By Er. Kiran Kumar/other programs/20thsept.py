# Question - 21 
# Write a program To check whether the given character is lowercase alphabet.
given_character = input("Enter a character :")
if given_character.islower():
    print("The given character is a Lowercase Alphabet.")



# Question - 22
# Write a program to check whether the given character is digit.

given_character = input("Enter a character :")
if given_character.isdigit():    # or isnumeric()
    print("The Given Character is a Digit.")


# Question - 23 
# Write a program to check whether the given character is alphabet
given_character = input("Enter a character :")
if given_character.isalpha():
    print("The given character is an Alphabet.")
    
    
# Question - 24 
# Write a program to check whether the given character is a special character.

given_character = input("Enter a character :")
if not given_character.isalnum():   # there is no direct method to check for special character
    print("The given character is a Special Character.")
    
    
# Question - 25 
# Write a program to check whether the given collection is List

given_collection = eval(input("Enter a collection :"))   # 'kiran' --- kiran
# print(type(given_collection))
if type(given_collection) == list:
    print("The given collection is a list.")
    
    

# Question - 26   (******)
# Write a program to check whether the entered value is default.

entered_value = eval(input("Enter a value :"))
if bool(entered_value) == False:
    print("The entered values is default.")




# Question - 27 
# Write a program to check whether The list consists of even number of values.
entered_list = eval(input("Enter a list :"))   
if len(entered_list) % 2 == 0:
    print("The entered list consists of even values.")




# Question - 28 
# Write a program to check whether a list consists of middle value.
# lists consists of middle value means, the lenght should be odd. 
entered_list = eval(input("Enter a list :"))
if len(entered_list) % 2 != 0:      #not equal sybmol is  ( != )
    print("The entered list consists of middle value. ")






# Question - 29 
# Write a program to check whether the entered input is Immutable.
entered_input = eval(input("Enter an input :"))
if type(entered_input) in [int,float,complex,bool,str,tuple]:    # total - 6 data types are immutable
    print("The entered input is Immutable")




# Question - 30 
# Write a program to check whether the entered input is mutable. 
# mutable means, the type should be in [list,set,dict]
entered_input = eval(input("Enter an input :"))
if type(entered_input) in [list,set,dict]:
    print("The entered input is Mutable")




# Question - 31 
# Write a program to check whether The entered input is a single value.
entered_input = eval(input("Enter an input : "))   # True, 3.4, 3, 2+9j 
if type(entered_input) in [int, bool, complex, float]:
    print("Entered Input is a Singe Value")
    





# Question - 32 
# Write a program to check whether the entered input is multivalue or not.
entered_input = eval(input("Enter an input :"))
if type(entered_input) in [list, tuple, dict, set, str]:
    print("The entered input is a multivalue")




# Question - 33 
# Write a program to check whether the entered number is having only single Digit.....means lenght is 1. 

entered_digit = input("Enter a number :")  # 123
if len(entered_digit) == 1:
    print("The entered number is having only single digit.")


    
    














