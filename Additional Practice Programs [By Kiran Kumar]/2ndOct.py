# Check Entered Collection has less than or equal to 5 elements or not

collection = eval(input("Enter any collection : "))
if len(collection) <= 5:
    print("The entered collection has less than or equal to 5 Elements")
else:
    print("The enterd collection doesn't has less than or equal to 5 Elements")
    



# Type of Character Entered is - Uppercase, Lowercase, Numbers or Special Characters (Using Method -1)

character = input("Enter any character : ")
if 'A' <= character <= "Z":
    print("Uppercase")
elif 'a' <= character <= 'z':
    print("Lowercase")
elif '0' <= character <= '9':
    print("Numbers")
else:
    print("Special Characters")
    
    
    
# Type of Character Entered is - Uppercase, Lowercase, Numbers or Special Characters (Using Method - 2)
character = input("Enter any character : ")
if character.isupper():
    print("Uppercase")
elif character.islower():
    print("Lowercase")
elif character.isnumeric():
    print("Numbers")
else:
    print("Special Character")
    
    
# Check the user entered data is single value data type or a collection
data = eval(input("Enter any data : "))
if type(data) in [int,float,complex,bool]:
    print("It's a Single Value Data Type")
else:
    print("It's a Collection")
    
    
# Entered Number is Two Digit Number or Not - Without Using Any Method
number = int(input("Enter any number :"))
if (9<number<100) or (-9<number<-100):
    print("Number is of Two Digit Number ")
else:
    print("Number is not a two digit number")


# Entered Number is Two Digit Number or Not - With Using len Method
number = input("Enter any number :")
if len(number) == 2:
    print("Two Digit Number")
else:
    print("Not a Two Digit Number")
