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
    
