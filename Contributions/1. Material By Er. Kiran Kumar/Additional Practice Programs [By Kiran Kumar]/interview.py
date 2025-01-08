

'''

Why Python is Interpreted. 
Write a program in the given list item into a single string. 
Write a program to remove duplicate elements 
OOPs Concepts 
Difference between Set & Dictionary 

Exception Handling 
How thread class create another thread class. 
Difference between Method Overloading & Method Overiding. 
What is Encapsulation 
Difference between list & set 

Find the 2nd largest number in an array 
Swap the number without using 3rd variable 
Reverse a string 
Find the duplicate in a string 


Difference between Drop & Duplicate 
When we use flash back 
Rules of EF Codd 
Explain Joins and types of Joins 
Explain Sub Query 

Scenario Based Questions 

Explain Agile Model 

'''









# Write a program in the given list item into a single string.  

my_list = [1,2,3,"kiran",3.4]
my_string = ""
for item in my_list:
  my_string = my_string + str(item)
  
print(my_string)
  
  
  
  
# Write a program to remove duplicate elements from a list 
my_list = [1,2,2,1,1,2]
new_list = []
for item in my_list:
  if item not in new_list:
    new_list.append(item)
print(new_list)


# Difference between Set & Dictionary 

# Set - It is a data structure that can store any number of elements, that is unordered in nature, it can only store unique elements. 
    #  - It can store values. 
# Dictionary - It is ordered, that can store any number of elements. 
            # - It can store unique key. 

# set()  - for typecasting  - empty set - set() -- unique values -- unordered.
# dict() - for typecasting  - empty dictionary - {} --- unique keys --- ordered 


my_dict = {"name":"Kiran", "age": 23}
my_dict["post"] = "Software Developer"
print(my_dict)


my_set = {1,2,3}
my_set.add(4)  # add function to add the element 
print(my_set)



# Find the 2nd largest number in an array  
array = [10, 1, 15, 2,3,4]
first = sorted(array)
print(first[-2])


# method - 2 (Without any method)
array = [10, 1, 15, 2,3,4]
first = 0
for item in array:
  if item > first: 
    first = item 
array.remove(first)
print(array)
second = 0
for item in array: 
  if item > second:
    second = item 
print(second)
   
  
    



# to solve programming questions ---- I need paper/pen & solitude.  ---- I can solve any questions. 



# Swap the number without using 3rd variable  
num1 = 10 
num2 = 20 
num1, num2  = num2, num1 
print(num1, num2)


# Reverse a string 
my_string = "kiran"  # narik
index = len(my_string)
# print(index)
reverse = ""
for item in range(index-1, -1, -1): 
  # print(my_string[item])
  # print(my_string[item])
  reverse = reverse + my_string[item] 
print(reverse)
  




# Find the duplicate in a string  
my_string = "Kiran Kumar"
new_string = ""
duplicate = ""
for char in my_string: 
  if char not in new_string:
    new_string = new_string + char 
  else: 
    duplicate = duplicate + char 
print(duplicate)