
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
  
  
  
  
  
  
  
  


# Question - 9 : Given Number is Prime or Not.
given_number = int(input("Enter a Number : "))  # 5 
flag = True  #  I am assuming that, the given number is Prime
for num in range(2,given_number):
  if given_number%num == 0:
    flag = False
    break
if flag == True:
  print("Prime Number")
else:
  print("Not a Prime Number")
  
  



# Question - 10 : Prime Number between 1 to 100 
# Lovely Question ---(*************) (Revision is must)


start = 1
end = 100 
count = 0
for num in range(start, end+1):
  # print(num)  # 2 
  if num > 1: 
    prime = True 
    for fact in range(2,num):
      if num % fact == 0:
        prime = False
    if prime == True:
      count = count + 1
      print(num)
    
print(f"Total {count} number of Prime Numbers in between {start} and {end}")


num = 5
for fact in range(2,num):
  if num % fact == 0:
    print(num)
    
    
    
    
  


# Question - 11 : Strong Number. 
# Sum of factorial of each digit is equal to given number. 
# Example - 145  
# 1! = 1, 4! = 24 , 5! = 120  
# 1+24+120 =  145
# 145 == 145 --- Hence, it is a strong number.

given_number = int(input("Enter a Number : ")) # 143 
temp = given_number # 143 
sum = 0 

while given_number > 0:  #143>0   # 14>0
  last = given_number % 10   # 3  # 4
  fact = 1
  while last > 0:  # 3>0   # 2>0  # 1>0
    fact = fact * last # fact = 1*3 = 3  # fact=3*2 = 6  # 6*1 = 6
    last = last - 1 # 3-> 2 # 2-> 1  # 1-> 0
  sum = sum + fact  # 0 + 6 = 6
  given_number = given_number // 10 
  
# print(temp)  
# print(sum)
  
if temp == sum:
  print("Strong Number.")
else:
  print("Not a Strong Number.")
    








# Question - 12 : Armstrong Number. 
# Sum of Power to the length of each digit. 

# number = 1236 
# length = 4
# 1**4 + 2**4 + 3**4 + 6**4  == 1236  (This is what we need to check )
# the sum of power of length to each digit should be equal to that number, then only it is armstrong number.




given_number = int(input("Enter a Number : "))
temp = given_number 
length = len(str(given_number))
armstrong = 0

while given_number > 0:
  last = given_number % 10 
  armstrong = armstrong + last**length
  given_number = given_number // 10 
  
if temp == armstrong:
  print("Armstrong Number.")
else:
  print("Not an Armstrong Number.")
  