
# Question 1 - Product of  each digits from the number. 

given_number = int(input("Enter a Number : "))  # 123 
product = 1

while given_number > 0:
  last = given_number % 10 
  product = product * last 
  given_number = given_number // 10 
  
print(product)