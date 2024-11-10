#  Disarium Number 
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
