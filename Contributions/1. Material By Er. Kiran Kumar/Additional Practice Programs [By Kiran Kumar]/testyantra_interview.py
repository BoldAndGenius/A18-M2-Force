
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
 