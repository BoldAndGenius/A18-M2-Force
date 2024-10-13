'''  Armstrong Number'''
#  An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits in the number.
#  153 (3 digits):
#  1^3 + 5^3 + 3^3 = 1 + 125 + 27  = 153 , So 153 is armstrong Number.
#  9474 (4 digits):
#  9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474 , So 9474 is armstrong Number.

num = int(input("Enter a number: "))
original_num = num  
length = len(str(num)) # To calculate no of digits in Number
sum = 0

# Loop to calculate the sum of the digits raised to the power of the length
while num > 0:
    rem = num % 10
    sum += rem ** length
    num //= 10  

if original_num == sum:
    print(f"{original_num} is an Armstrong number")
else:
    print(f"{original_num} is not an Armstrong number")



''' Perfect_Number '''
#  A perfect number is a positive integer that is equal to the sum of its factors excluding the number itself.
#  Example:
#  num=28
#  sum_of_factors= 1 + 2 + 4 + 7+ 14 = 28
#  So 28 is a Perfect_Number

num=int(input("Enter a Number:"))
sum_of_factors=0
for factor in range(1,num):
    if num % factor == 0:
        sum_of_factors += factor
if sum_of_factors == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")



''' Strong Number '''
#  If a number is a strong number then its sum of the factorial of its digits equals the original number.
#  Example: num = 145
#  sum_of_factorials = 1! + 4! + 5! = 1 + 24 + 120 = 145 
#  num == sum_of_factorials, so num is Strong Number


num = int(input("Enter a number: "))
original_num = num
sum_of_factorials = 0

# Loop until num becomes 0
while num > 0:
    rem = num % 10 
    fact = 1

   # Calculate factorial of the last digit
    for n in range(1, rem + 1):
        fact *= n
    sum_of_factorials += fact  
    num //= 10  
if original_num == sum_of_factorials:
    print(f"{original_num} is a strong number")
else:
    print(f"{original_num} is not a strong number")



''' Happy Number '''
#  Happy numbers are positive integers that eventually lead to 1 through the process of summing the squares of their digits.
#  Example:
#  num = 19
#  sum_of_squares = 1^2 + 9^2 = 1 + 81 = 82 , 8^2 + 2^2 = 64 + 4 = 68 , 6^2 + 8^2 = 36 + 64 = 100 , 1^2 + 0^2 + 0^2 = 1 .Since we reached 1, 19 is a happy number.
#  If they fall into a cycle and never reach 1, they are classified as non-happy numbers.
#  Example:
#  num = 20
#  sum_of_squares = 2^2 + 0^2 = 4 , 4^2 = 16 , 1^2 + 6^2 = 1 + 36 = 37 , 3^2 + 7^2 = 9 + 49 = 58 , 5^2 + 8^2 = 25 + 64 = 89 .....
#  Here we won't get 1 as sum_of_squares but the loop ends when we get a number that's already in the list.So,20 is not a happy number.


num = int(input("Enter a number: "))
original_num = num
# List to keep track of numbers we are already having to prevent infinite loops
numbers = []
while num != 1 and num not in numbers:
    numbers.append(num)
    sum_of_squares = 0

    # Calculate the sum of the squares of its digits
    while num > 0:
        digit = num % 10
        sum_of_squares += digit ** 2
        num //= 10
    num = sum_of_squares  # Update num to the new sum of squares

if num == 1:
    print(f"{original_num} is a happy number")
else:
    print(f"{original_num} is not a happy number")


''' Magic Number '''
#  A magic number is  a number for which the repeated sum of its digits results to 1.
#  Example:
#  num = 19
#  sum_of_digits : 1 + 9 = 10 , 1 + 0 = 1 .Now we have reached 1, so 19 is a magic number.


num=int(input("Enter a number:"))
original_num = num

while num >= 10:  # Repeat until the number is a single digit
    sum_of_digits=0
    
    # Sum the digits
    while num > 0:
        rem = num % 10
        sum_of_digits += rem
        num //= 10
    num = sum_of_digits # Update num with the sum of its digits

if num == 1:
    print(f"{original_num} is a magic number")
else:
    print(f"{original_num} is not a magic number")


''' Disarium Number '''
#  A Disarium number is a number in which the sum of its digits, each raised to the power of its respective position ,is equal to the number itself.
#  The positon will start from 1.
#  Example:
#  num = 175
#  sum_of_digits = 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175
#  Sum of the digits raised to the power of their positions equals the number.So, 175 is disarium number.


num = int(input("Enter a nmuber:"))

# Convert the number to a string to access individual digits
str_num = str(num)

position=1  # Initialize the position to 1 at starting

result=0
for digit in str_num:
    result += int(digit)**position  # Convert the character digit to integer , Because we can't peerform operation between string and integer
    # Increment the position for the next digit
    position += 1   

if num == result:
    print(f"{num} is a disarium number")
else:
    print(f"{num} is not a disarium number")

