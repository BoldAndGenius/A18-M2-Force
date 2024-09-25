# Question - 1
# Python Program to find ASCII Value of Character and Vice Versa

# Character to ASCII Value 

entered_character = input("Enter a Character :")  # 'a'
ascii = ord(entered_character)   #  97
print(f"The ASCII Value of {entered_character} = {ascii}")



# ASCII Value to Character 
ascii2 = int(input("Enter an ASCII Value :"))  # 97
character = chr(ascii2)   # 'a'
print(f"The Character Value of {ascii2} = {character} ")






# Question - 2
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
'''
Decimal = Base is 10
Binary = Base is 2
Octal = Base is 8
Hexadecimal = Base is 16
'''

decimal_value = int(input("Enter a Decimal Value"))
binary = bin(decimal_value)
octal = oct(decimal_value)
hexadeci = hex(decimal_value)

print(f"The Binary Value is {binary},\nThe Octal Value is {octal},\nThe hexadecimal Value is {hexadeci}")






# Question - 3
# Python Program to Build a Calculator

num1 = float(input("Enter a number 1 :"))
num2 = float(input("Enter a number 2 :"))
operator = input("Choose an Operator - [ +, -, *, /, //, **, %  ] :")
if operator == "=":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "//":
    print(num1 // num2)
elif operator == "**":
    print(num1**num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid")
    
    
    
# Question - 4  [[[ Revise ]]]
# Python Program to find number is Prime or Composite 

'''
Prime Number - have two divisors only.  eg - 2,3,5,7,9
Composite Number - more than two divisiors.  eg - 4,6,8

'''

num = int(input("Enter a number : "))
# I have to divide this number from 1 to that number, if get more than two divisors, then prime. Otherwise not prime.  ---- to divide in series....therefore use loop
count = 0
index = 1
while index<= num:    # 1<10
    if num % index == 0:     # 10%1 == 0
        count = count + 1
    index = index + 1
if count == 2:
    print("Prime Number ")
else:
    print("Composite Number")
    
    
    
    


# Question - 5 
# Find Sum of Elements in a List

list = [1,2,3,4,5]

# Method - 1 : Using Build in Method 
print(sum(list))

# Method - 2 : Using For Loop
list = [1,2,3,4,5]
sum = 0
for i in range(0,len(list)):
    # print(i)  - prints index
    # print(list[i])  - prints index's value 
    sum = sum + list[i]
print(sum)


# Method - 3 : Using While Loop
list = [1,2,3,4,5]
sum = 0
index = 0
while index < len(list):
    sum = sum + list[index]
    index = index + 1
print(sum)
