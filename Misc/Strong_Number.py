#  Strong Number
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
