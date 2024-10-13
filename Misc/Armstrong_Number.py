#  Armstrong Number
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
