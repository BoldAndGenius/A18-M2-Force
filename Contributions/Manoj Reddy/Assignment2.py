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

# Q10. Write a program to check whether a number is prime or not using while loop.

num = int(input("Enter Number: "))
prime = True
for factor in range(2,num):
    if num % factor == 0:
        prime = False
        break
if prime == True:
    print("Prime Number")
else:
    print("Not Prime Number")
        