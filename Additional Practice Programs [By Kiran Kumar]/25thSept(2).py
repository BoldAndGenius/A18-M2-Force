# For Loops Question -

# Write a Python program that finds the maximum element in a list using a for loop.

list1 = [1,2,3,4]
for i in list1:
    # print(i)
    #let's assume the first index value or the first element is the maximum number
    max = list1[0]
    if i > max:
        max = i
print(max)
    




# Question - 2
# Write a Python program that counts the number of vowels in a given string using a for loop.

given_string = "kiran@kumar"
# first access element by element - therefore use for loop
count = 0
for i in given_string:      # syntax is,  for variable in range/collection    [here string is a collection]
    # print(i)  # we get each character
    # now just check the character.
    if i in 'aeiouAEIOU':
        count = count+1
print(f"The number of vowerls = {count}")





# Question - 3
#  Write a Python program that uses a for loop to print the multiplication table of a given number up to 10.
number = int(input("Enter a number :"))
for i in range(1,11):
    # print(i)
    print(i*number)
    
    

# Question - 4 
# Write a Python program that calculates the factorial of a given positive integer using a for loop.


number = int(input("Enter a number :"))  # 3
fact = 1
for i in range(1,number+1):
    # print(i)
    fact = fact * i  # fact = 1*1 = 1,   fact = 1*2 = 2,  fact = 2*3 = 6,  
print(f"The factorial of {number} is {fact}")




# Question - 5 
# Write a Python program that takes a list of numbers as input and uses a for loop to calculate and print the sum of all the elements in the list.

list1 = []
elements = int(input("Enter number of Elements to be entered :")) # 4
for i in range(0,elements):
    # print(i)
    element = int(input())
    list1.append(element)
# print(list1)
# list1 = [1,2,3,4,5]
sum = 0
for i in list1:
    sum = sum + i
print(f"The Sum of List is : {sum} ")

