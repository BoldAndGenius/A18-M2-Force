'''Q1. Write a program to print the following using while loop
a. First 10 Even numbers
b. First 10 Odd numbers
c. First 10 Natural numbers
d. First 10 Whole numbers        '''

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

''' Q2. Write a program to print first 10 integers and their squares using while loop. '''

start = 1 
integers = []
squares = []
while start <= 10:
    integers+=[start]
    squares+=[start**2]
    start+=1
print(f"Integers:{integers}")
print(f"Squares:{squares}")

Q3. Write while loop statement to print the following series: 10, 20, 30 ... ... 300

