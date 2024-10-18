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
    
    
    
    

# All Fancy Number Program - 4 : Check if a number is Harshad/Niven Number or Not.
# Harshad Number / Niven Number =>  A number which is divisible by sum of it's digits.
# eg.  156 =>  1+5+6 = 12     156 is divisible by 12  (It means, jab 156 ko divide kare 12 se to remainder zero aai)

num = int(input("Enter a number : "))
temp = num
sum = 0
while num>0:
    last = num % 10
    sum = sum + last
    num = num // 10
    
if temp % sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
    
    
    

# All Fancy Number Program - 5 : Check if a number is Duck Number or Not.
# Duck Number => A number which has zeroes present in it.  Eg. 402, 290

num = int(input("Enter a number : "))
count = 0
while num>0:
    end = num % 10
    if end == 0:
        count = count + 1
    num = num // 10
    
if count > 0:
    print("Fancy Number.")
else:
    print("Not a Fancy Number.")