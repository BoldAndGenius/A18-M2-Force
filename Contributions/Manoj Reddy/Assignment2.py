# Q1. Write a program to print the following using while loop
# a. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers        

even = 1
even_numbers = []
while even <= 20:
    if even % 2 == 0:
        even_numbers.append(even)
    even+=1
print(even_numbers)

odd = 1
odd_numbers = []
while odd <= 20:
    if odd % 2 :
        odd_numbers.append(odd)
    odd+=1
print(odd_numbers)

start = 1
natural_numbers = []
while start <= 10:
    natural_numbers.append(start)
    start+=1
print(natural_numbers)

start = 0
whole_numbers = []
while start < 10:
    whole_numbers.append(start)
    start+=1
print(whole_numbers)

# Q2. Write a program to print first 10 integers and their squares using while loop. 

start = 1 
integers = []
squares = []
while start <= 10:
    integers+=[start]
    squares+=[start**2]
    start+=1
print(f"Integers:{integers}")
print(f"Squares:{squares}")

# Q3. Write while loop statement to print the following series: 10, 20, 30 ... ... 300 

start = 10
end = 300
series = []
while start <= end:
    series.append(start)
    start += 10
print(series)

# Q4. Write a while loop statement to print the following series 105, 98, 91 .........7.

start = 105
end = 7
series = []
while start >= end:
    series.append(start)
    start -= 7
print(series)
    
# Q5. Write a program to print first 10 natural number in reverse order using while loop.

start = 11
end = 1
rev_order = []
while start > end:
    start -= 1
    rev_order.append(start)
print(rev_order)

# Q6. Write a program to print sum of first 10 Natural numbers.

start = 1
end = 10
sum = 0
while start <= end:
    sum+=start
    start+=1
print(sum)

# Q7. Write a program to print sum of first 10 Even numbers.

start = 1
end = 20
even_sum = 0
while start <= end:
    if start % 2 == 0:
        even_sum+=start
    start+=1
print(even_sum)

# Q8. Write a program to print table of a number entered from the user.

start = 1
end = 10
num = int(input("Enter Number: "))
while start <= end:
    print(f"{num}X{start}={num*start}")
    start += 1

# Q9. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
start = min(num1,num2)
end = max(num1,num2)
even_numbers = []
while start <= end:
    if start % 2 == 0:
        even_numbers.append(start)
    start += 1
print(even_numbers)

# # Q10. Write a program to check whether a number is prime or not using while loop.

num = int(input("Enter Number: "))
prime = True
if num < 2:
    prime = False
else:
    for factor in range(2,num):
        if num % factor == 0:
            prime = False
            break
if prime == True:
    print("Prime Number")
else:
    print("Not Prime Number")
    
## Q11. Write a program to find the sum of the digits of a number accepted from the user.

num = int(input("Enter Number: "))
sum = 0
while num != 0:
    last_digit = num%10
    num = num//10
    sum+=last_digit
print(sum)

# Q12. Write a program to find the product of the digits of a number accepted from the user.

num = int(input("Enter Number: "))
product = 1
while num != 0:
    last_digit = num%10
    num = num//10
    product = product*last_digit
print(product)

# Q13. Write a program to reverse the number accepted from user using while loop.

num = int(input("Enter Number: "))
rev = 0
while num != 0:
    last_digit = num%10
    num = num//10
    rev = rev*10+last_digit
print(rev)

# Q14. Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One

num = int(input("Enter Number: "))
final = []
if num == 0:
    print("Zero")
else:
    while num != 0:
        last_digit = num%10
        num  = num//10
        new_num = str(last_digit)
        nums = {'1':"One",'2':"Two",'3':"Three",'4':"Four",'5':"Five",'6':"Six",'7':"Seven",'8':"Eight",'9':"Nine",'0':"Zero"}
        output = nums.get(new_num)
        final.insert(0,output)
print(final)

nums = int(input("Enter Number: "))
new_num = str(nums)
for num in new_num:
    if num == "0":
        print("Zero")
    elif num == "1":
        print("One")
    elif num == "2":
        print("Two")
    elif num == "3":
        print("Three")
    elif num == "4":
        print("Four")
    elif num == "5":
        print("Five")
    elif num == "6":
        print("Six")
    elif num == "7":
        print("Seven")
    elif num == "8":
        print("Eight")
    else:
        print("Nine")
    
# Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.

series = [0,1]
num = int(input("Enter Number: "))
if num == 1:
    print(series[0])
elif num == 2:
    print(series[1])
else:
    for i  in range(num-2):
        fib = series[-1]+series[-2]
        series.append(fib)
    print(series)

# Q16. Write a program to print the factorial of a number accepted from user.

num = int(input("Enter Number: "))
factorial = 1
n = 1
while n <= num:
    factorial*=n
    n+=1
print(factorial)

# Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)

num = int(input("Enter Number: "))
string = str(num)
count = len(string)
amstrong_num = 0
digit = int(string)
while digit != 0:
    last_digit = digit%10
    digit = digit//10
    amstrong_num = amstrong_num+last_digit**count
if num == amstrong_num:
    print("Its Armstrong Number")
else:
    print("Not Amstrong Number")


# Q18. Write a program to add first n terms of the following series using a while loop: 1/1! + 1/2! + 1/3! + ........ + 1/n!

num = int(input("Enter Number: "))
factorial = 1
sum = 0
i = 1
while i <= num:
    factorial*=i
    sum+=1/factorial
    i+=1
print(sum)

# Q19. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.

sum = 0
while True:
    num = input("Enter Number or quit: ")
    if num.lower() == 'quit':
        break
    sum+=int(num)
print(sum)

## Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered.
  
postive = []
negative = []
while True:
    num = int(input("Enter Number: "))
    if num == 0:
        break
    else:
        if num<0:
            negative+=[num]
        else:
            postive+=[num]
print(f"Postive Numbers count is {len(postive)}")
print(f"Negative Numbers count is {len(negative)}")  

# Q21. Write a program to find the HCF of two numbers entered from the user.

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
