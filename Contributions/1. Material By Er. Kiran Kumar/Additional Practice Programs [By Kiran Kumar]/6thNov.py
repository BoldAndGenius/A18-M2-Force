class Human:
    hands = 2
    eyes = 2 
    bones = 206 
    
    def __init__(self):
        print("Object is Created")
        
    
sannidhi = Human()  
# output  - Object is Created
# we can explicitly call the __init__ method as well












class Human:
    hands = 2
    eyes = 2 
    bones = 206 
    
    # we will use this to store data, at the time of object creation (beneficial for us)
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def happyness(self,num):
        print(f"Feeling Happy {num}%")
    def sadness(self,num):
        print(f"Feeling Sad {num}%")
        
    
'''
ClassDict = {
    "hands":2,
    "eyes":2,
    "bones":206,
    
    "happyness":address1,
    "sadness":address2,
    "add_info":address3
}


'''
    
# pass the argument in class call (like a function)
sannidhi = Human("Sannidhi Shetty",23)    # automatically call the __init__ method, and store the argument value into it.

#explicity calling the __init__ method using the object.
sannidhi.__init__("Sannidhi Shetty", 23)  # Human.__init__(sannidhi, "Sannidhi Shetty", 23)

divya = Human("Divya Anaparthi",22)


# __dict__   act like a variable.
# __dict__ is used to see the dictionary.
print(Human.__dict__)  # Output - Class Dictionary.(since Human class is used)
print()
print(sannidhi.__dict__)  # Output - Object Dictionary (since sannidhi object is used)
print(divya.__dict__)   # Output - Object Dictionary.




'''
Class Dictionary - 

{'__module__': 'builtins', 'hands': 2, 'eyes': 2, 'bones': 206, '__init__': <function Human.__init__ at 0x0000019F3BA72DE0>, 'happyness': <function Human.happyness at 0x0000019F3BA72F20>, 'sadness': <function Human.sadness at 0x0000019F3BA72FC0>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}


Object Dictionary - 
{'name': 'Sannidhi Shetty', 'age': 23}
{'name': 'Divya Anaparthi', 'age': 22}


'''
