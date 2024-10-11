# 85. Write a program.To check the type of a given character.

character = input("Enter any character : ")
if 'a'<=character<='z' or 'A'<= character<= "Z":
    print("Alphabets")
elif '0'<character<='9':
    print("Digits.")
else:
    print("Special Characters")
    
    
 
# Question No. 86   
# Write a program to consider an integer number. Print happy if the number is divisible by two. Print SAD if the number is divisible by 5 and print square of the numbers only if it is divisible by seven else print the number as it is.


number = int(input('Enter any number : '))
if number%2 == 0:
    print("Happy.")
if number%5==0:
    print("Sad.")
if number%7==0:
    print(number*number)
else:
    print(number)