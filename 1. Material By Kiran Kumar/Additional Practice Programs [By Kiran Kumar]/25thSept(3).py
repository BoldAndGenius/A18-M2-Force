# While Loop 

# Write a Python program that uses a while loop to calculate the sum of digits of a given positive integer.
# # Example input
# n = 12345


given_integer = 8911
# to get the sum of digits, we need to individually access the each elements, and then add it.
sum = 0
while given_integer > 0 :
    last = given_integer % 10   # to get the last digit
    sum = sum + last
    given_integer = given_integer // 10    # remove the last

print(sum)





# Write a Python program that reverses a given positive integer using a while loop.
number = 1234
rev = 0
while number > 0:
    last = number % 10   # 4  ,  3  , 2  , 1
    rev = rev * 10 + last  # 4 , 43 , 432 , 4321
    number = number // 10   # 123 , 12  , 1
    
print(rev)