

# Complete OOPs. 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Object Oriented Programming System /Strucutre  ---- It is a way of writing code! 
# It's a programming paradigm --- No one is forcing to write code in OOPs, you can write in procedural & functional as well, but it is not scalable. ....when you want to create scalable products, that time OOPs will help you a lot. 
# ML & AI -- end to end projects are made using Python, here we use OOPs concepts a lot. 

'''
1. Procedural/Functional Approach is not a lot helpful for real world case.

Prodcedural -- code in line by line  -- sum of two numbers.
Functional -- inside the functions -- code reuse.


Google, Amazon, Startup, Goldman ---- always working on their code ...constantly evolving --- if code has a good structure, then it is better.
# code that can be expanded.
# you can build upon the already written codes.

# millions of sellerr ---- it's not good to create that much variable or put in list....we need some template, which we can use it multiple times....based on the new sellers. 

'''


# It is always helpful if we could create a blueprint of what we want and then create multiple copies via it. 
# casting -- make product.   [inspired by the real life]

'''
So, OOPs help us in doing below things...
1. Define our own data type.
2. Generality to Specificity.

OOPs is thus a programming paradigm, which help us to write better code. 

'''


# OOPS Topics 
'''

Total we have 6 Topics only.....

1. Class.
2. Object.
3. Encapsulation.
4. Inheritance.
5. Polymorphism.
6. Abstraction.

'''


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Class 

'''
1. Blueprint.
2. Self-defined Data Type. 

Let us see some example of known  data type.


Class is a blue print of an object. 
It's a template to create an object. 

'''

a = 4 
print(type(a))
# <class 'int'>

b = 3.4 
print(type(b))
# <class 'float'>

c = 'kiran'
print(type(c))
# <class 'str'>
c.upper()  # upper() is a method in the str class. 


# All data types are built-in Classes in Python. 
# Already the developer of Python, write the class for int, float, complex, bool, str, list, tuple, set, dict


# Inside class,we has two things --- 1. Data/Attributes/Property. 
                              # ---  2.Behaviour/Method.
                              

# for example - Car 
# 1. Data/Attributes/Property  --- color, brand, name, top speed. 
# 2. Behaviour/Method ------------accelerate(), brake(), start(), 
                    
                
                
mylist = [1,2,3,4,5] # these are property
mylist.append(6)  # .append() is a method of mylist class 
print(mylist)




c = 5 + 8j
# below two are not the methods 
print(c.real)  # real part  # 5.0
print(c.imag)  # imaginary part  # 8.0






# Syntax to create a Class 

'''

class <ClassName>:
    ...
    
'''

# Creating our own Class - 
class Car:
    pass 

print(Car) # <class 'Car'>    -- now this become one data type 



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++