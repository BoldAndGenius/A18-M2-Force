# Check Entered Collection has less than or equal to 5 elements or not

collection = eval(input("Enter any collection : "))
if len(collection) <= 5:
    print("The entered collection has less than or equal to 5 Elements")
else:
    print("The enterd collection doesn't has less than or equal to 5 Elements")
    



# Type of Character Entered is - Uppercase, Lowercase, Numbers or Special Characters

character = input("Enter any character : ")
if 'A' <= character <= "Z":
    print("Uppercase")
elif 'a' <= character <= 'z':
    print("Lowercase")
elif '0' <= character <= '9':
    print("Numbers")
else:
    print("Special Characters")