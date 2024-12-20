# OOPS 
# The full form of OOPS is Object Oriented Programming System 


'''
Why we need OOPS? 

- There are three type of Programming Approaches - 
1. Procedural Programming -- where we direclty write the process to solve the problems.
                          -- It is good for simple programs, as the complexity of programes increases, this procedural programming will not work. A lot of code will be there, unable to manage properly. 
    Suppose, you need to find the sum of two numbers.....you write the logic in 4 lines, let's suppose again after 100 lines of code....you need to again want sum of two numbers, so you will again write the 4 lines of code again.........so lines of code get's increased........hence, complexity of prorams gets increased....and line of code also increased.....and in this code, code redundancy is there...you are writing the same code again and again................so this programming approach is not good for complex projects or problem.
    
    So, to solve this problem.........We introduced Functional Programming Approach.
    
    
2. Functional Programming -- In this approach, whatever code that we gonna use in the further programs...we will put into a function, and everytime when we need it........we call the function.
- Functional approach help us to reuse the code. 
- But in this approach there is still one loophole, that is .....it doesn't provide data security.
- CSE field is all about Data, if our data is not secure...then what's the use of this programming.
So, to solve this problem of data securty....we introduced a new concept of programming...that is OOPs.

3. Object Oriented Programming System --- It's a programming system, where we use the concept of object.
                                      -- Objects are the real world entitity, we can see it, we can feel it.
                                      -- Objects are the instance/product of a class. 
                                      -- Class is a blue print of an object. 
                                      -- This approach provides, data security....it also help us to maintain our code....our code become more redable....more flexible..we can add the functionality or remove the functionality...
                                      but in procedural programming, if we add the addition logic....10 timce, and in between if I need to remove this logic and do subtraction, it becomes difficult to do in 1000 lines of code....so ...this problem is solved by the OOP approach.  

- OOPs reduces the problem of Code Maintenance.
- It reduces the Code Complexity.
- It decreased the Complexity.
- It increases the Redability. 

- Highly helpful for Django (for Developers), Hybrid Framework (Testers).




Real world example for OOPs -
- Suppose I want to open my Car Company...to start with, first I will create a design or blueprint of that car, so that blueprint or desing is called a Class (It'a desing, It's a blueprint)....It's like my imagination..it's not real my car.

To create that car, I wil give it to engineers, those enginners...create my car using the blueprint..
So, that car is an object.....(it's a real world entitity)...we can feel it, we can use it. 

So, The product we get is an object. and the Desing or blueprint is a Class. 


Now, How to create a class - 
Use class keyword, and then the classname in PascalCase, then use colon (:), and inside it write the class properties. 

'''
# class keyword, classname in Pascalcase 
class MyCar: 
    # inside a class, whatever we write is a Property.
    # Property is a combination of Variables and Methods. 
    # Property is of two types --- Class Properties, Object Properties.
    # Class Properites are of two types --- 
    # Class Properties are the Properties that are common to all the objects.
    # Object Properties are the Properties that are unique to individual objects. 
    # The below 5 are variables
    height = "6ft"
    width = "12ft"
    wheels = 5 
    mirrors = 3 
    enginer = "300 CC"
    
    # A function inside a class is called Method. 
    # The below is a function.
    def accelerate(self):    # self is a tax we need to pay, if I need to declare a function inside a class 
        print("Accelearting!")

        
        
'''
- Each time you create a class, a Class Dictionary gets created.
- Each time you create an Object, an Object Dictionary gets created --- Empty Dictionary. 


- If you use Object, 1st it go to object dictionary.....it is empty....not present in it, then it go to class dictionary. It will checks in Class Dictionary.
- If it is not present in Class Dictionary, It will give an exception. 


- Keep Object in mind, and create a class. 



'''



class Human: 
    a = 100 
    hands = 2 
    eyes = 2 
    ears = 2 
    legs = 2 
    
    def ego (self, num):
        print(f"Feeling Ego {num} %")
        
    def general_info(self,height,weight, iq):
        self.height = height 
        self.weight = weight 
        self.iq = iq 
        
    def random(self,a,b):
        self.a = a   # go inside object dictionary, (since self is having object's address), inside object dictionary ....key 'a' gets created ...and the value 'a' will be provided as a value, that we are passing in the function's arguments.  
        self.b = b 



# Object Creation  -- call the Class and assign it to a variable 
# as object is created...an empty object dictionary is created..
Shazzy = Human()  # as you call the class, an object reference is created...and we are assigning the object reference into a variable called Shazzy.
# not this variable is having the object reference, so using this object reference we can access the contents of the class. 
# if we directly try to access the contents of the class, we will get the error.
 
# print(legs) -- here we will get a NameError, because legs is not defined ....
# general_info() -- here we will get a NameError, because this function is not defined...
# So, to use the content of the class...either we need to use object or the class.
# Using object or Class, we can access the contents of the class. 

# Shazzy is an object, we created on line number 113  
# Using Object, if we need to access the contents of the class, then we need to use the dot operator 

print(Shazzy.a) # Shazzy is an object, dot means..we are going inside the object dictionary.... but right not object dictionary is empty, so it will check into the class dictionar...inside the class dictionary..there is a key "a", so it will returns the value of key "a"
## Output -  100 


print(Shazzy.random(10,30)) # first check in object dictionary, not found ...so go to class dictionary...there is a key name "random" is there, which is storing the random functions' address......so,random(10,30)....10, 30 value will stored in object class....as we did using self operator.....so new key value pair gets created. 
## Output -  None 
# reason ---   Shazzy.random(10,30) ---- it goes to random() function, and there it assigned in key value pair in a object dictionay......then this function is returning None......so at the place of Shazzy.random(10,30)....None will sit.........now we are printing None.........so None gets printed 

# print(None)    - None gets printed....so same way, in the above, Shazzy.random(10,30) place...None is sitted...and we print it. 





print(Shazzy.a)  # inside object dictionary, first check for a key..not fouund....then find in class dictiory...get it..then print the value 


print(Shazzy.c)  # inside object dictioary..there is no c key..then goes to clas dictionary..not found...so gets Exception or Error 
# AttributeError: 'Human' object has no attribute 'c' -------------- ******************************** Human is a class...not an object..but why it is saying...human object ?????




# we are assigning value 
Shazzy.c = 30  # first check in object dictionary..not found....so it will create a key value pair in object dictionary 
# When we are assigning, A new key value pair gets created in Object Dictionary (since we are using object )



"""

At the time of class creation...this class dictionary gets created 
Class Dictionary = {'a':100, 
                    'hands':2, 
                    'eyes': 2, 
                    'ears': 2, 
                    'legs':2 ,
                    'ego': ego_address_function's_address,
                    'random': random_function's_address ,
                    "general_info": general_function's_address}
                    
Object Dictionary = {}    -- at the time of creation, it is empty. 
# as we perform some operation....so it gets updated 

Object Dictionary = { 'a': 10,
                    'b': 20,
                    'c': 30 }
                    # this updation of value in object dictionary is done...because at the above we executed one line..that is 
                    Shazzy.random(10,20) -- inside the random() function..using self keyword...we are adding the key value pair as "a" as 10, "b" as 20. 
                    
                    # Shazzy.c = 30  -- here we created new key in object dictionary...as "c" and assigning a vlaue as 30.

"""

# print(Shazzy.hobbies) --- get attribute error -- this key is not present in object dictionary..then check in class dictionarlyy..there also not present this key...so gives attribute error. 


Shazzy.hobbies = ['dancing','study']  # Shazzy is an object...it first goes into object dicionary...check is there is any key 'hobbies' or not.....so no present...so it create a new key value pari...key as 'hobbies' and value as ['dancing', 'study']







##################################################### 

# Magic Methods  

'''

- start & end with __ (double underscore)
- you can't create magic methods, it is already present. 
-   __any __ 

- We just need to understand, How to use these Magic Methods. 
-  __init__   => Each time you create an object, Automatically __init__ function runs once. or invoked once. 


'''







class Human:
    hands = 2
    eyes = 4 
    fingers = 20 
    ears = 2
    nose = 1
    legs = 2 
    def ego(self,num):   # the first argumnet should be self -- whetere you use it or not 
        print(f"Feeling Ego {num}%")
    def anger(self, num):
        print(f"Feeling Anger {num}%")

   
# atleast one variable or 
# to declare an empty block of code, we use pass keyword. 
# if I don't know what are it's properties, put pass keyword or three dots - ...  (it is having the same meaning)
# it means you create an empty block
    
# after designing, you need to create an object --- by calling an object
class Random:
    pass 

# when you call a class..an object is created, and when you stored it....that variable has the reference of that object.

kiran = Human()  # kiran is an object of Human class. 
kunal = Human()
# kiran and kunal both are different object. 
# whey we created object --- usinh this object, I can get the content of the class 
# anger() -- directly I can't call the function

# print(legs) -- nameeroor -- not declare earlier -----legs is protected, I have to use object 
# with the help of objects we can get it....and then use dot operator. 
kunal.legs  # kunal object of that class, it goes inside (.)..and take the legs variable 
kiran.hands

print(kunal.legs)
print(kiran.hands)

kiran.anger(10)  # only give that argument that are present after the self 
# also can be written as 
# when using class, give value for self 
# self represent address of an object 
Human.anger(kiran,28)  # kiran is a self (first argument) kiran object shoule be frist created, ---- kiran






# Presentation  

class Jspider:
    name = "Kiran Kumar"
    age = 23 
    native = "Bihar"

    def sum(num1,num2):
        return num1 + num2 
    
    

def sum(num1,num2):
    print("Kiran is a good boy.")
    return num1 + num2

print("Ashish Kumar")






############################################################################# 



class Human: # pascalcase
    # properties --- eyes, hands, bones --- object properties 
            #    ---- happyness, sadness & info --- class properties 
    eyes = 2 
    hands = 2 
    bones = 206 
    
    #snakecase  - uses underscores to separate words in lowercase
    def happyness(self,amount):
        print(f"Feeling Happy {amount} %")
        
    def sadness(self, amount):
        print(f"Feeling Sad {amount} %")
        
    def info(self,name,age):
        self.name = name 
        self.age = age 
        
object1 = Human()
print(object1.eyes)
print(object1.hands)
print(object1.bones)
object1.happyness(10)
object1.sadness(90)
# print(object1.kiran)  get error 


kiran = Human()    # Object is ceated 
# kiran is an object or self ...we need to pass kiran as the first argument into the call
Human.info(kiran, "Kiran Kumar", 24)
print(kiran.name)
print(kiran.age) 







'''
In the given class `Human`, **object properties** and **class properties** are as follows:

### Class Properties:
- **Class properties (class variables)** are shared among all instances of the class. They are defined directly within the class body and are not tied to any specific instance.
  - `eyes = 2`
  - `hands = 2`
  - `bones = 206`

### Object Properties:
- **Object properties (instance variables)** are unique to each instance and are typically defined within methods using `self`.
  - `name` (defined in the `info` method)
  - `age` (defined in the `info` method)

### Explanation:
1. **Class Properties**:
   - `eyes`, `hands`, and `bones` are class-level variables because they are declared directly inside the class and not inside any method. These values are shared across all instances of the class.

2. **Object Properties**:
   - `name` and `age` are instance-level variables because they are defined inside the `info` method using `self`. Each object of the `Human` class can have its own unique `name` and `age`.

### Methods:
The methods `happyness`, `sadness`, and `info` are **instance methods** as they take `self` as their first parameter and operate on object properties or provide behavior specific to an instance.

---

Let me know if you’d like an example to clarify this further! 😊


'''











class Human: # pascalcase
      
    # def __init__(self):
    #     print("Object Created")
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
        
    


kiran = Human("Kiran Kumar", 23)
print(kiran.name)
print(kiran.age)

print(kiran.__dict__) # object dictionary
print(Human.__dict__)  # clas dictionary 





# __init__  -- automatically it gets called, when an object is created
# constructor will get exectued 
# I can call it using function name as well. 
# use for our advantage, store all the information...
# any order -- but practice is write it beginner 


# __init__

# __dict__   -- it will give you class & object dictionary 
# class.__dict__   -- class dictionary
# object.__dict__













class Bottle: 
    
    # print("Debugging1") # This gonna print no matter we call a class or not  
    colour = "blue"
    size = 8
    shape = "round"
    material = ['plastic','silicon','artificial agents']
    def manufacturing(self): # as python see def, it will ignore it..and execute the next lines
        print("Manufacturing is going on!")
    # print("Debugging2") # this get prints 

print(id(Bottle))  # 2858944448800   (Address of Class)
mybottle = Bottle()
print(mybottle) # <__main__.Bottle object at 0x000002BC0502C980>    # id of object reference 
                # hexadecimal 

# using dot operator, we can access the data members & member functions 
print(mybottle.colour) # blue
print(mybottle.size)  #  8 
print(mybottle.shape)  # round
print(mybottle.material) # ['plastic', 'silicon', 'artificial agents']
print(mybottle.manufacturing())  # Manufacturing is going on! and None

mybottle.manufacturing  # Manufacturing is going on!   (at the time of function call, only print statement gets printed)

# But when we print it.......it will print ...what is returning it...so therefore None 
print(mybottle.manufacturing())  #None
  
  
  
print(  )
# Accessing Contents (Variable & Functions) of a Class Using Classname 
print(Bottle.colour)  # blue 
print(Bottle.size)   # 8 
print(Bottle.shape)  # round
print(Bottle.material) # ['plastic', 'silicon', 'artificial agents']
print(Bottle.manufacturing(mybottle))  # Manufacturing is going on! None
Bottle.manufacturing(mybottle)  # Manufactur ing is going on!



# Accessing contents (Variable & Functions) of a Class using Object Nmae 
print(mybottle.colour)  # blue 
print(mybottle.size) # 8
print(mybottle.shape) # round 
print(mybottle.material) # ['plastic', 'silicon', 'artificial agents']
mybottle.manufacturing()  # Manufacturing is going on! 






# Magic Methods 
# Constructor 




class Employee: 
    name = "Kiran"
    age = 18 
    dob = "1 Dec 2004"
    # def __init__(self,name,age,jd):  
        # print(name,age,jd)
    
    def __init__(self,myname,myage,myjd):  
        # inside the object dictionary name key will be created, and value will be the name we provided
        self.name = myname 
        self.age = myage 
        self.jd = myjd 
        print("I am inside the Constructor")
        print(myname,myage,myjd)
        
    def func(self):
        print("My Function")


emp1 = Employee("kiran",20,"Software Developer")  # as object is created -- the constructor will automatically gets called 
# output -  kiran 20 Software Developer

print(emp1.name) # kiran
print(emp1.age) # 20
print(emp1.dob) # 1 Dec 2004
print(emp1.__init__)
# <bound method Employee.__init__ of <__main__.Employee object at 0x00000241056CE150>>

print(emp1.__init__("kiran",20,"Software Developer"))
# I am inside the Constructor
# kiran 20 Software Developer
# None    #I am printing it, so it will print the None, because it is returning None 







# Declare a Car Class 


class MyCar:
    height = "6f"
    width = "12f"
    wheels = 5 
    
    def accerate(self):
        print("Accelerating!!")
# Output  -- you will not get anything, 
# as python see the class keyword, it gets inside the class...for height, widhth & wheels -- memory will be created, as it see the def keyword, it will ignore the function..and it goes to next line..there is no next line, so it will go outside of the class ...therofre no ouput we get . 



class Human:
    eye = 2 
    nose = 1 
    lesgs = 2 
    def mood(self,num):
        print(f"Felling {5}%sad")
kiran = Human()
kiran.eyes
kiran.nose