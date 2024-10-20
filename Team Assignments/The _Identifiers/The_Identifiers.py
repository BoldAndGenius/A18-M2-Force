#Team Members:: K.Vengadesh
 #              C.NagaMaheshKumar
  #              P.Pavithra 
# #  # Q1. Write a program to print the following using while loop
 #a. First 10 Even numbers
count=1
start=2
while count<=10:
     print(start,end=" ")
     start+=2
     count+=1
print()

# # # b. First 10 Odd numbers
count=1
start=1
while count<=10:
     print(start,end=" ")
     start+=2
     count+=1
print()
    
# # # c. First 10 Natural numbers
start=1
while start<=10:
     print(start,end=" ")
     start+=1
print()

# # # d. First 10 Whole numbers
start=0
while start<10:
     print(start,end=" ")
     start+=1
print()
    
# # # Q2. Write a program to print first 10 integers and their squares using while loop.
start = 1  
while start <= 10:
     print(f"{start}^2 = {start ** 2}")  
     start += 1  
    
# # # Q3. Write while loop statement to print the following series: 10, 20, 30 … … 300
start=10
while start<= 300:
     print(start, end=" ")
     start += 10 
print()

# # # Q4. Write a while loop statement to print the following series 105, 98, 91 ………7.
Start = 105
while Start >= 7:
     print(Start, end=" ")
     Start -= 7 
print()

# # # Q5. Write a program to print first 10 natural number in reverse order using while loop.
start= 10 
end=1
while start>= end:
     print(start, end=" ")
     start -= 1  
print()

# # # Q6. Write a program to print sum of first 10 Natural numbers.
start = 1 
sum= 0  
while start <= 10:
     sum += start 
# #     start += 1
# # print(f"Sum of first 10 natural numbers: {sum}")


# # # Q7. Write a program to print sum of first 10 Even numbers.
# # count = 1
# # start= 2
# # sum = 0 
# # while count <= 10:
# #     sum += start 
# #     start += 2
# #     count += 1  
# # print(f"Sum of first 10 even numbers: {sum}")


# # # Q8. Write a program to print table of a number entered from the user.
# # num = int(input("Enter a number: ")) 
# # start= 1 
# # while start<= 10:
# #     print(f"{start} x {num} = {num * start}")  
# #     start+= 1  
    
# # # Q9. Write a program to print all even numbers that falls between two numbers (exclusive both
# # # numbers) entered from the user using while loop.
# # start = int(input("Enter the first number: "))
# # end = int(input("Enter the second number: "))
# # if start > end:
# #     start, end = end, start
# # num = start + 1  
# # while num < end:
# #     if num % 2 == 0: 
# #         print(num, end=" ")
# #     num += 1  
# # print()

# # # Q10. Write a program to check whether a number is prime or not using while loop.
# # num= int(input("Enter a number: "))
# # Start = 2  
# # is_prime = True  
# # while Start  < num :  
# #     if num % Start == 0:
# #         is_prime = False
# #         break  
# #     Start  += 1  
# # if is_prime and num > 1:
# #     print(f"{num} is a prime number.")
# # else:
# #     print(f"{num} is not a prime number.")

# # # Q11. Write a program to find the sum of the digits of a number accepted from the user.
# # num = int(input("Enter a number: "))
# # sum = 0
# # while num != 0:
# #       sum += num % 10  
# #       num //= 10  
# # print(f"The sum of the digits of a user entered number : {sum} .")  


# # # Q12. Write a program to find the product of the digits of a number accepted from the user.
# # num = int(input("Enter a number: "))
# # product=1
# # while num != 0:
# #      product *= num % 10 
# #      num //= 10  
# # print(f"The product of the digits of a user entered number : {product} .")  

# # # Q13. Write a program to reverse the number accepted from user using while loop.
# # num = int(input("Enter a number: "))
# # reverse = 0 
# # while num !=0:
# #     reverse = reverse * 10 + num %10
# #     num //= 10 
# # print(f"The Reversed number : {reverse} .")  

# # # Q14. Write a program to display  number names of the digits of a number entered by user,
# # # for example if the number is 231 then output should be Two Three One
# # num = int(input("Enter a number: "))
# # digit_names = ["Zero", "One", "Two", "Three", "Four", 
# #                "Five", "Six", "Seven", "Eight", "Nine"]
# # result = ""
# # while num != 0:
# #      digit = num % 10  # Extract the last digit
# #      result = digit_names[digit] + " " + result  # Prepend the name
# #      num //= 10  # Remove the last digit
# # print(f" The number names of the digits of a user entered number : {result} .")


# # # Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using while
# # # loop.
# # n = int(input("Enter the number of terms in the Fibonacci series: "))
# # a, b = 0, 1
# # print("Fibonacci series:")
# # count = 0
# # while count < n:
# #     print(a, end=" ")
# #     a, b = b, a + b  
# #     count += 1   


# # # Q16. Write a program to print the factorial of a number accepted from user.
# # num = int(input("Enter a number to find its factorial: "))
# # factorial = 1 
# # count = 1      
# # while count <= num:
# #     factorial *= count  # Multiply the current count with factorial
# #     count += 1         
# # print(f"The factorial of {num} is: {factorial}")

# # # Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a
# # # number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)
# # num = int(input("Enter a number to check if it is an Armstrong number: "))
# # original_num = num
# # sum_of_cubes = 0
# # while num > 0:
# #     digit = num % 10 
# #     sum_of_cubes += digit ** 3 
# #     num //= 10  
# # if original_num == sum_of_cubes:
# #     print(f"{original_num} is an Armstrong number.")
# # else:
# #     print(f"{original_num} is not an Armstrong number.")

# # # Q18. Write a program to add first n terms of the following series using a while loop:
n = int(input("Enter the value of n: "))
fact = 1
sum = 0
initial = 1
while initial <= n:
     fact *= initial 
     sum += 1 / fact
     initial+=1
print(f"The sum of the first {n} terms of the series is: {sum}")

# #  Q19. Write a program to enter the numbers till the user wants and at the end it should display
# #  the sum of all the numbers entered.
number=int(input("How many number want to add :"))
totalsum =0
n=1
while n<=number:
       start = int(input(f"enter a num {n} :"))
       totalsum+=start
       n+=1
print(f"Total sum is :{totalsum} ")
#         #    (or)
sum = 0
while True :
      num = int(input("enter a num:"))
      if num==0:
          print(f"sum of the numbers:{sum}" )
          break
#      else:
#       sum +=num
#      continue

# # Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should
# #  display the count of positive and negative numbers entered.
# positivenumcount = 0
# negativenumcount = 0
# stop = "stop"
# while True:
#      num = eval(input("enter a num(0 to stop):"))
#      if num == stop : 
#          print(f"Total positive numbers: {positivenumcount}")
#          print(f"Total negative numbers: {negativenumcount}")
#      elif num == 0:
#          break
#      elif num > 0:
#          positivenumcount +=1
#      elif num < 0:
#          negativenumcount +=1
#      elif num == stop : 
#          print(f"Total positive numbers: {positivenumcount}")
#          print(f"Total negative numbers: {negativenumcount}")





