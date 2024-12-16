# 30 Most Asked Python Interview Questions 




# Question - 1
# What is your most preferred laguage  - Python 

# What makes Python different from other languages ?  or  # Why Python? 
# They want to know, why the developer choose this language. 


'''

Python is an interpreted language.
Dynamic.
High Level Programming Language.
It's an Object Oriented Language.
Easy to understand & learn.
Easy syntax.
Automatic & Effective Memory Management.   (automatic garbage collection.)



Dynamic means, the type of the variable is determined only during run time, Hence one variable can have different data types at different times. Data Types are checked during execution. 

High level language means, that python is easy to read, manages memory for you, works on any system. 

Provides tools that let you focus on solving problems, instead of dealing with hardware.


'''











# Question - 2 
# What do you mean by Python being an Interpreted Language. 

'''
An interpreter allows the code to run line by line rather than being compiled into machine code first. 
This is why, Python is easy to debug. 

we can take an analogy, while cooking a food...we take one step at a time, not worrying to cook the food in a one go. 

'''








# Question  3
# Give three difference between Lists & Tuples  



'''

Lists Vs Tuples - 

1.Square Brackets are used in Lists, and Tuples uses Parenthesis.
2.Lists are Mutable, whereas Tuples are Immutable.
3.Lists occupies more memory as compared to a Tuple. 
4.List has slower iteration compared to Tuples, But it is better for insertion & deletion operations due to it's mutability.
(Reason - Lists are dynamic in nature, Tuple is static in nature...Tuple has a fixed memory...so very fast to iterate over the tuple...but for lists, it is dynamic in nature...so extra memory blocks will be there for isertion and deletion, because of dynamic behaviour.... to iterate over lists, it takes more time as compared to tuple.)


Use tuples when you don’t need to modify the data (immutability).
Use lists when you need flexibility in adding/removing elements.

'''









# Question  4
# Differentiate between Mutable and Immutable Data Types or What is Mutability? 

'''

Mutable Data types - These are the data types, that can be modify after the creation.
For eg - List, Set & Dictionary. 

list = [1,2,3]
we can change the value 2 to 5 
list[1] = 5   # at 1st index, add an element 5
print(list) # [1,5,3]

We can use append(4) , pop(element)

Mutable data types are required where we need frequent update. 




Immutable Data Types - For these data types, once it is created there won't be any modificitions into it.

eg - string, tuple, single value data type 

tuple = (1,2,3)
tuple[0] = 5   # Error 
print(tuple) 


Immutable data types are useful, where we don't want any frequent changes. 
'''