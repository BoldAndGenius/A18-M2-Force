

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
- It is passed whenever we are calling any method.
- Only an object can access or helpful in connecting attributes and methods inside our class. 

'''



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import keyword 
print(keyword.kwlist)





# Difference between Function & Method.

# Function -- It is define outside of the class.
        #  -- It is call directly.
        
# Method   -- It is defint inside the class.
#          -- It is call using an object.

def func(num1,num2):
    return num1 + num2 
print(func(10,20))  # 30  # directly calling it

class Sum:
    def func(self,num1, num2):
        return num1 + num2
obj = Sum()  # 
print(obj.func(20,30))
# Sum.func(obj,20,30)  -- it gets converted to like this. 



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Creating our first class 

class Student:
    def __init__(self):
        name = "Kiran" # it is having a local scope, we can print in this __init__ function, but we can't access outside the function.
        # dekho agr hame batana hai yeh student ka roll number yeh hai...to ham pehle ek student ko pakrenge and then we will say.......tera roll number yeh hai..and name yeh hai...........so same way, to do this....we will use 'self' .  aapka name Kiran hai....self.name = "Kiran"...and aapka roll number 10 hai.....  self.rollnumber = 10 
        
        # now this "name" & "roll number" is not made in this function...
        # it is made in the student instance.....on that address
        # now we can use 'name' and 'roll number' outside of the class using the 'object reference'. 
        
        
    
    

class Student:
    def __init__(self):
        self.name = "Kiran"
        self.rollnum = 1 
        self.add = "Bangalore"
stu1 = Student()
print(stu1.name, stu1.rollnum, stu1.add)
# Kiran 1 Bangalore

stu2 = Student()
print(stu2.name, stu2.rollnum, stu2.add)
# Kiran 1 Bangalore

# Now for the both object (stu1 & stu2), we are getting the same Name, rollnumber & address....so it is not right. 
#As this doesn't make sense...




# Agr school me new student aaiga...to vo apne name batega...so let's create this thing that....every student will have their name and all.
# it should be define by the user. 



class Student:
    def __init__(self, name, rollnum, marks):
        self.name = name 
        self.rollnum = rollnum 
        self.marks = marks 
        
stu1 = Student("Kiran", 1, 90)
print(stu1.name,stu1.rollnum, stu1.marks)

stu2 = Student("Kajal",2 , 98)
print(stu2.name,stu2.rollnum, stu2.marks)



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# Creating Methods 

class Student:
    def __init__(self,name, rollnum, marks):
        self.name = name 
        self.rollnum = rollnum 
        self.marks = marks 
        
    def study(self):
        # self is a link between variable & method, If I want to tell that Kiran is playing...so first I need to go to Kiran...and then tell he is playing...same way....first self.name will give Kiran....(that object)
        print(f"{self.name} is Playing.")
        # we can not directly access the object Kiran
        
    def play(self): 
        print(f'{self.name} is Playing.')    
        

stu1 = Student("Kiran", 1, 90)
stu1.study()
# Kiran is Playing.

stu2.play()
#Kajal is Playing.



stu2 = Student("Kajal",2 , 98)
stu2.study()
# Kajal is Playing.

stu2.play()
# Kajal is Playing.


# self is the bridge, because of which everything gets initialized and get used. 




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# Complex Number Class 



# Question 1: Class for Complex Numbers

"""
Create a Python class named `ComplexNumber` to represent complex numbers.

Theory:
A complex number is a number that comprises a real part and an imaginary part.
It is typically written in the form a + bi, where 'a' is the real part,
and 'b' is the imaginary part, and 'i' is the imaginary unit (√-1).

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Comparison (==, !=)



Test Cases:
Test Case 1:
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, -2)
assert str(complex1) == "3+4i"
assert str(complex2) == "1-2i"
assert str(complex1 + complex2) == "4+2i"
assert str(complex1 - complex2) == "2+6i"
assert str(complex1 * complex2) == "11-2i"
assert str(complex1 / complex2) == "-1.0+2.5i"
assert complex1 != complex2

Test Case 2:
complex3 = ComplexNumber(-2, 5)
complex4 = ComplexNumber(2, 3)
assert str(complex3) == "-2+5i"
assert str(complex4) == "2+3i"
assert str(complex3 + complex4) == "0+8i"
assert str(complex3 - complex4) == "-4+2i"
assert str(complex3 * complex4) == "-16-1i"
assert str(complex3 / complex4) == "1.0+i"
assert complex3 != complex4



"""








a = 5 
print(type(a))  # <class 'int'> 
print(type(int))  # <class 'type'>  

# 5 is an object of int class, and int is an object of type class. Because int is a type. 





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
Magic Methods - 

They are the special methods in Python which are defined inside the class.
They begin and end with double underscore (__)
They have a special where in they get called themselves.
creation - __init__
print -   __str__
+  -  __add__
-  - __sub__
*  - __mul__
/  - __trudiv__
// - __floordiv__

'''



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

s1 = Student("Kiran", 23)
s2 = Student("Kajal", 21)

s1.name 
s2.name 

# s1 & s2 above are instance variable which have different values of attribute  
# s1 & s2 are different instance of a particular class. --- they have different values. 


# object is...calling a class, how many times you call a class, that much time the object get created.















'''

Hey there, Python enthusiasts! Are you ready to take your coding skills to the next level? In this comprehensive video, we're diving headfirst into the world of Object-Oriented Programming (OOP) - a fundamental paradigm that will revolutionize the way you write and structure your Python programs. 

Get ready to unlock a whole new dimension of Python mastery!

What's in store for you in this OOP extravaganza?
✅ Understand the core concepts of OOP, including classes, objects, attributes, and methods
✅ Explore the principles of encapsulation, inheritance, polymorphism, and abstraction
✅ Learn how to create your own custom classes and objects from scratch
✅ Discover the power of inheritance and how it can help you write DRY (Don't Repeat Yourself) code
✅ Dive into the world of method overriding, method overloading, and operator overloading
✅ Gain insights into access modifiers, static methods, and class methods
✅ See OOP in action through real-world examples and practical applications

💡 Key Takeaways:
Organize your code into logical, reusable components using classes
Leverage inheritance to build upon existing functionality and create hierarchies
Implement polymorphism to write flexible, adaptable, and maintainable code
Understand the importance of abstraction and encapsulation for data protection
Apply OOP principles to tackle complex programming challenges with ease

'''