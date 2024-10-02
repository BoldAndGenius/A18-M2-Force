''' 
Q1. Write a program to print the following using while loop
a. First 10 Even numbers
b. First 10 Odd numbers
c. First 10 Natural numbers
d. First 10 Whole numbers
Q2. Write a program to print first 10 integers and their squares using while loop.
Q3. Write while loop statement to print the following series: 10, 20, 30 … … 300
Q4. Write a while loop statement to print the following series 105, 98, 91 ………7.
Q5. Write a program to print first 10 natural number in reverse order using while loop.
Q6. Write a program to print sum of first 10 Natural numbers.


Q9. Write a program to print all even numbers that falls between two numbers (exclusive both
numbers) entered from the user using while loop.

Q12. Write a program to find the product of the digits of a number accepted from the user.
Q13. Write a program to reverse the number accepted from user using while loop.
Q14. Write a program to display the number names of the digits of a number entered by user,
for example if the number is 231 then output should be Two Three One
Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using while
loop.

Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a
number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)
Q18. Write a program to add first n terms of the following series using a while loop:
1/1! + 1/2! + 1/3! + …….. + 1/n!
Q19. Write a program to enter the numbers till the user wants and at the end it should display
the sum of all the numbers entered.
Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should
display the count of positive and negative numbers entered.






'''


# Q7. Write a program to print sum of first 10 Even numbers.
# num = int(input("Enter a number for which you want to print the even numbers :"))
num = 18
sum = 0
for i in range(0,num+1,2):
    print(i) #- for validation 
    sum = sum + i
print(f"The Sum of first 10 even numbers is ",sum)


# Q8. Write a program to print table of a number entered from the user.
number = int(input("Enter a number for which you want to print the table :"))
for i in range(1,11):
    print(number * i)





# Q10. Write a program to check whether a number is prime or not using while loop.
number = int(input("Enter a number : "))
prime = True
for num in range(2,number):
    if number%num == 0:
        prime = False
if prime == True:
    print("Prime Number ")
else:
    print("Not a Prime Number")



# Q16. Write a program to print the factorial of a number accepted from user.
num = int(input("Enter a number for which you want to find the factorial : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of a {num} is {fact}")




# Q11. Write a program to find the sum of the digits of a number accepted from the user.

number = int(input("Enter any number : "))  # 123
rev = number
start = 1
sum = 0
while start<=number:
    end = number % 10 
    sum = sum + end 
    number = number // 10 

print(f"The sum of digits in a {rev} is {sum}")

