# Elif Statement -

# Question - 54 :
# Write a program to check the relation between two integer numbers
num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))

if num1 > num2:
    print(f"{num1} is greatest.")
elif num1 < num2:
    print(f"{num2} is greatest.")
else:
    print(f"{num1} and {num2} is equal.")



# Question - 55 :
# Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it.

enter_character = input("Enter a Character :")
if enter_character.isupper():
    print("Uppercase")
elif enter_character.islower():
    print("Lowercase")
elif enter_character.isdigit():
    print("Number")
else:
    print("Invalid")



# Question - 56 :
# Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.

character  = input("Enter a character :").lower()  # a
list1 = []
if character in 'aeiou':
    print("Vowel")
    list1 = list1 + [character]   # [] + [a]  => [a]  #list concatenation 
    print(list1)
else:
    print("Consonant")
    print(ord(character))     # ord()  function is used to get the ascii value of that character
    
    
    
    
# Question - 57 :
# Write a program to check whether a given character is uppercase. If it is uppercase, convert it to lowercase.Else PRINT LOWERCASE.
given_character = input("Enter a character :")
if given_character.isupper():
    print("Uppercase")
    # given_character.lower()    
    print(given_character.lower())  ##char.lower() is way to make your character lowercase
else:
    print('Lowercase')
    


# Question - 58 :
# Write a program to checkWhether the entered character is a number. If it is a number, print the ASCII value of that number.
entered_character = input("Enter a character ")  # '1'
if entered_character.isnumeric():
    print("The enterd character is Digt or Number.")
    print(ord(entered_character))

# ord function is used to find the ascii value of any character.
# ord fucntion is used to find the ascii value of any character.
# ord () function is used to find the ascii value of any chracter. 


# Question - 59 
# Write a program to check whether given character is uppercase, print its lowercase character or if given character is lowercase print its uppercase character or if given character is special character print the character after adding 8 to the ascii value of that particle special character


given_character = input("Enter a character :")
if given_character.isupper():
    print(given_character.lower())
elif given_character.islower():
    print(given_character.upper())
else:
    print(chr(ord(given_character) + 8))   # logic was -       chr( ord(given_character) + 8 )




# Question - 60 
# Write a program to check whether the last character of a given string is a special character or not.


given_string = input("Enter a string :")
if not given_string[-1].isalnum():
    print("Last Digit is a Special Character")

