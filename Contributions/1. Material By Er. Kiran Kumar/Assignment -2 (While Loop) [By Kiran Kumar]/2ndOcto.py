


# Q1. Write a program to print the following using while loop
# a. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers

start = 0
end = 18
while start<= end:
    print(start)
    start = start + 2
    
start = 1
end = 20
while start<= end:
    print(start)
    start = start + 2
    
start = 1
end = 10
while start<= end:
    print(start)
    start = start + 1
    
start = 0
end = 9
while start <= end:
    print(start)
    start = start + 1









# Q2. Write a program to print first 10 integers and their squares using while loop.

# Assuming first 10 positive integers 
start = 1
end = 11
while start<end:
    print(start," ", start**2)
    start = start + 1
 
 
# Q3. Write while loop statement to print the following series: 10, 20, 30 … … 300

start = 10
end = 300
while start<= end:
    print(start)
    start = start + 10


# Q4. Write a while loop statement to print the following series 105, 98, 91 ………7.

start = 105
end = 7
while start >= end:
    print(start)
    start = start - 7



# Q5. Write a program to print first 10 natural number in reverse order using while loop.

start = 10
end = 1
while start>= end:
    print(start)
    start = start - 1




 
# Q6. Write a program to print sum of first 10 Natural numbers.
sum = 0
for i in range(1,11):
    sum = sum + i
    print(i)
print(f"The sum of first 10 natural number is :",sum)
    

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




# Q9. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.

# from 0 to 10 --- 2,4,6,8
start = int(input("Enter the Starting Point :"))
real_start = start + 1
end = int(input("Enter the Ending Point :"))
while real_start < end:
    if real_start % 2 == 0:
        print(real_start)
    real_start = real_start + 1





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


# Q12. Write a program to find the product of the digits of a number accepted from the user.
number = int(input("Enter a number : "))  # 123
rev = number
start = 1
product = 1
while start<=number: 
    end = number % 10 
    product = product * end
    number = number // 10 
print(f"The Product of a digits of {rev} is {product}")
    


# Q13. Write a program to reverse the number accepted from user using while loop.

number = int(input("Enter a number : "))  # 123
# temp = number 
rev = 0
while number > 0:
    end = number % 10   # 3  # 2
    rev = rev*10 + end  # rev = 0*10 + 3 = 3   # rev = 3*10 + 2 = 32 
    number = number // 10   # 12
print(rev)


# Q14. Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One


number = input("Enter a number : ") # '231' 

for num in number:  # '2'
    if num == "1":
        print("One", end=" ")
    elif num == "2":
        print("Two", end=" ")
    elif num == "3":
        print("Three", end=" ")
    elif num == "4":
        print("Four", end=" ")
    elif num == "5":
        print("Five", end=" ")
    elif num == "6":
        print("Six", end=" ")
    elif num == "7":
        print("Seven", end=" ")
    elif num == "8":
        print("Eight", end=" ")
    elif num == "9":
        print("Nine", end=" ")
    elif num == "0":
        print("Zero", end=" ")
    
    










# Q16. Write a program to print the factorial of a number accepted from user.
num = int(input("Enter a number for which you want to find the factorial : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of a {num} is {fact}")



