

# Class Method -- We need to pass "Class Reference" as an first argument, cls is a convention to pass (that is the class reference)
#              -- We need to use decorator called @classmethod 
#              -- Can be accessed by using Both Class & Object both. 

class Human:
    eyes = 2 
    nose = 1
        
    @classmethod 
    def processing(cls):
        print(f"{cls} is processing...")
    
# Using Class, I am accessing.
Human.processing()  # <class 'Human'> is processing...
# What about the 'cls' argument...we are not passing here, it stills work ??? (****)
    
    

# Using Object also, I can access.

kiran = Human()
kiran.processing()  # <class 'Human'> is processing...
# Python converts to -   Human.processing(kiran) ---- (****) -- but kiran is an object...how it is having class reference ???
# Is python, converts like this.....???? (*****)

        
        
# Class Method -- It can be accesssed by using both class & object.

# Object Method -- It can be only accesssed by object. 
# Why Object Methods can't be accessed by using Class ??? --- Because firstly the flow goes to object dictionary...and then the class dictionary.....if we are directly checking in the class dictionary...so we will not be able to go bottom..or th object dictionary to see what's going on.