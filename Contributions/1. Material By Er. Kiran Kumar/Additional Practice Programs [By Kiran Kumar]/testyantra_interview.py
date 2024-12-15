
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