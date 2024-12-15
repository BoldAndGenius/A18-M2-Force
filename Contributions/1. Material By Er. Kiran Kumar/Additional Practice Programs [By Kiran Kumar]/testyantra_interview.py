
# Question 1 - Product of  each digits from the number. 

given_number = int(input("Enter a Number : "))  # 123 
product = 1

while given_number > 0:
  last = given_number % 10 
  product = product * last 
  given_number = given_number // 10 
  
print(product)



# Question - 2 : Factorial of a Number.

number = int(input("Enter a Number : ")) # 5 =>  5*4*3*2*1 
fact = 1
while number > 0:
  fact = fact * number 
  number = number - 1
print(fact)
 






# Question - 3 : Fibonacci Series of the given number 
# Series : 0,1,1,2,3,5.....
# Index  : 1,2,3,4,5

# means, for number = 3, it should print the series as -  0,1,1 

# Fibonacci Series means, first and last number is 0 & 1 respectively, and the next term will be addition of previous two terms.

given_number = int(input("Enter a Number : ")) # 3 
index = 1
first = 0
second = 1
third = 0

while index <= given_number:
  print(first)
  third = first + second 
  first = second 
  second = third 
  index = index + 1
  
  






# Question - 4 : Print nth fibonacci series.
# Series - 0,1,1,2,3,5,8,13
# index -  1,2,3,4,5,6,7,8    (very important..use for traversing)

# nth fibonacci means.....suppose he wants what is the 3rd fibonacci series --- it means what is the third term ..or the third index. 



nth_fib_num = int(input("Enter the number for which you want to find the fibonacci series : "))
first = 0
second = 1 
third = 0 

index = 1
while index <= nth_fib_num:
  if index == nth_fib_num:
    print(first)
  third = first + second 
  first = second 
  second = third 
  index = index + 1
  
  
  

# Question - 5 : Reverse of a Number


user_number = int(input("Enter a Number : "))
reverse = 0 

while user_number > 0:
  last = user_number % 10 
  reverse = reverse * 10 + last 
  user_number = user_number // 10 
  
print(reverse)








# Question - 6 : Given Number is Palindrome or Not 

given_number = int(input("Enter a Number : "))   # 1234 
temp = given_number 
reverse = 0 

while given_number > 0:
  last = given_number % 10 
  reverse = reverse * 10 + last 
  given_number = given_number // 10 
  
if temp == reverse:
  print("Palindrome")
else:
  print("Not a Palindrome")
  
  
  
  
# Question - 7: Factorial of a Number 

number = int(input("Enter a Number : "))  # 3 
fact = 1
while number > 0:
  fact = fact * number
  number = number - 1
  
print(fact)





# Question - 8 : Factorial range between 11 to 20.
# It means, for 11 to 20, for each number tell the factorials.... 11!, 12!, 13!, 14!....20! 

# (Revise *********************) -- good question.



starting_range = 11 
ending_range = 20 

while starting_range <= ending_range:
  fact = 1
  temp = starting_range
  
  

  while temp > 0:
    fact = fact * temp 
    temp = temp - 1
  print(fact)
  
  starting_range = starting_range + 1