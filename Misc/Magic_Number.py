#  Magic Number
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

