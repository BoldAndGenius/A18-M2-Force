'''

List Comprehensions

Question: Write a Python list comprehension that generates a list of all numbers between 1 and 100 that are divisible by both 3 and 5.
Bonus: Modify the comprehension to include only those numbers where the sum of their digits is greater than 5.



Create a Python list containing the numbers 1 to 5. Write a script to print the list in reverse order.


Given a string s = "Hello, World!", write a Python script to convert the string to all lowercase letters and then print it.


Write a Python script that takes a user's age as input and prints whether they are a child (age < 18), an adult (18 ≤ age < 65), or a senior (age ≥ 65).


Write a Python loop that prints the numbers from 1 to 10, but for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". If a number is a multiple of both 3 and 5, print "FizzBuzz".

'''




# Exchange the values of two numbers with & without using a temporary variable 
# With Temporary Variable

num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
# color bucket example -- use this logic
temp = num1
num1 = num2
num2 = temp
print(f"The first number is {num1}")
print(f"The second number is {num2}")



# Without Temporary Variable
# we can use Arithmetic Operation for that 
num1 = int(input("Enter a number 1 :"))  # num1 = 10
num2 = int(input("Enter a number 2 :"))  # num2 = 20

num1 = num1 + num2  # num1 = 30  -- this is used for swapping!

num2 = num1 - num2  # num2 = 30 - 20 = 10 
num1 = num1 - num2  # num1 = 30 - 10 = 20
# wow, swapping done! 

print(f"The first number is {num1}")
print(f"The second number is {num2}")