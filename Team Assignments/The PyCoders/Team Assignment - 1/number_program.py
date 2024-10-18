# Print all digits of a number on different lines 

num = int(input("Enter a number : "))  # 1234
while num>0:
    last = num % 10 
    print(last)
    num = num // 10
    
    
    
# All Fancy Number Program - 1 : Check if a number is Palindrome or not 

num = int(input("Enter a number : "))
temp = num
reverse = 0

while num>0:
    last = num % 10 
    reverse = reverse + num 
    num = num // 10
if reverse == temp:
    print("Palindrome Number.")
else:
    print("Not a Palindrome.")
    
    
# All Fancy Number Program - 2 : Check if a number is Spy Number or Not 
# Spy Number =>  sum of it's digits == product of it's digits
# Eg. 123 is a Spy Number =>   1+2+3 = 6   and 1*2*3 = 6     6 == 6

num = int(input("Enter any number: "))
sum = 0
product = 1
while num>0:
    last = num % 10 
    sum = sum + last
    product = product * last
    num = num // 10
if sum == product:
    print("Spy Number.")
else:
    print("Not a Spy Number.")
    


# # All Fancy Number Program - 3 : Check if a number is Special Number or Not.
# Special Number => Sum of Digits + Product of Digits = Original Number
# 59 =>   5 + 9 + 5 * 9 = 59 

num = int(input("Enter a number: "))
temp = num
sum = 0
product = 1
while num>0:
    end = num % 10
    sum = sum + end
    product = product * end 
    num = num // 10
    
if sum + product == temp:
    print("Special Number.")
else:
    print("Not a Special Number.")