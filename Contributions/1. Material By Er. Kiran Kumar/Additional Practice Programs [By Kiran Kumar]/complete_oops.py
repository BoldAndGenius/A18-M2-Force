

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




# What is an Object  

'''

Object is an instance of our Class.
Everything in Python is an Object. 

a = 5 
5 is an instance of int class. 


var = 3+7j 
print(type(var))  # 3+7j is an object of complex class. 
#Hence in Python, everything is an object of some class. 

'''


def func(num1,num2):
    return num1 + num2 

print(type(func))    # <class 'function'>   
# func() is ab object of class function. 


# Everything in Python is an Object.
# Everything in Python is an Object.
# Everything in Python is an Object.
# Everything in Python is an Object.
# Everything in Pytho is an Object.
# Everything in Python is an Object.
# Everything in Python is an Object.
# Everything in Python is an Object.
# Everything in Python is an Object. 



# How to create an Object of our Class - 
# To create an object, We have to call the Class. 


class Car:
    pass 

swift = Car()
print(type(swift))   # <class 'Car'>
# swift is an object of Car class. 

# we never write like this  swift = Car()
# we directly writ,   a = 10    -- it automatically creates the object of int class.
# print(type(a))  # <class 'int'>   -- it is an object of class int
# to create list, we directly write  list = [], for tuple we write  tuple = ()
# the reason for this...why we not call the class and do it. 
# Python tells.........I have created all these classes inside me.....I know, how it works...I know everything about these classes...me aapko enko seedha banane dunga using object literal. 
# object literal means....you can direclty use these shortcuts...  a = 10 ....but at the same time, eska matlab yeh nahi ki purane vala method false hai. 


a1 = int()
print(a1) # 0 
print(type(a1))  # <class 'int'>
# the above method is right....but to make it easy...it creates an object literal.
# when you use [], I will get to know that it's an object of list class.
# whey you put decimal value, it's an object of float class.
# when you put in quotes, it's an object of str class.
# () - tuple, {} - set,  {key:value} - dict 
# I know about these classes, so don't worry...you don't need to call it.



# woh ! (****)
num = int(5)
print(type(num)) # <class 'int'>
print(num)  # 5 

# the above is same as 
num = 5 
print(num)  # 5
print(type(num))  # <class 'int'>



# Python gives us "Object Literal" for Built in types.  



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





# Creating Our First Class 


# id()  - returns the identity of an object. 



class Student:
    def __init__():
        pass 

s1 = Student()
# s1 goes to constructor thta is.. __init__(s1) and get initiliazed.
# you can verify it 




def myfunc(arg):
    print(id(arg))

s1 = 2 
myfunc(s1)
print(id(s1))
# the id of "s1" and "arg" is same, that is what means is....s1 goes to arg place. Since id is same. 
#140715068295640
# 140715068295640



class Student:
    def __init__(arg):
        print(id(arg))
    
s1 = Student()
print(id(s1))
# id of both s1 & arg is same......hence it means, s1 goes to constructor to get initialized ....and it is logical as well, since after constructing all these.. we need an object...at the end we are doing these things for the object only....right. 
# 2760106701840
# 2760106701840
# and for this reason only, we can give any name to it.......but majority everywhere we use "self" ....because 's1'object is itself going and getting initialized....itself...so they used self! 

# Everytime you create an object, the constructor call once. 

# when you open an application, at the starting only...it checks do it have an internet or not...if no, it gives error. 

# Koi bhi cheez jab aapko create karne se pehle hi check karni hai...then go for Constructor. 

'''
Advantage/Application of Constructor - 
1. Background check in Companies -- before joining, they did it.
2. Internet check for apps --- uber app, without intenet it gives error.
3. Configuration related checks before sharing. 

It's like a receptionist which checks and add/gives all informtion required. 


# Self - 
- self is the reference to the object, created for our class.
- It is passed whenever we are calling any function.
- Only an object can access or helpful in connecting attributes and methods inside our class. 

'''



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++