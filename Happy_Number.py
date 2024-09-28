#  Happy Number
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
