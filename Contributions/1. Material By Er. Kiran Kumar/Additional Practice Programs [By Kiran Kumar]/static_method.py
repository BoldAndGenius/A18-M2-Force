

# Static Method  -- No need to pass the self keyword, we need to decorate the function with the help of @staticmethod.

# Static Methods can be accessed by both class & object.


class Human:
    eye = 2 
    nose = 1
    # Object Method 
    def feelings(self,name,value):
        print(f"{name} is feeling {value} % Happy")
    
    #Static Method
    @staticmethod
    def processing():
        print("It is a Static Method.")
        

# Using Object, I am calling the Static Method
Kiran = Human()
Kiran.processing()  # It is a Static Method.
# Python converts into -  Human.processing() -- it should not take any argument, since it is a staticmethod
                    #  Where Kiran gets stored ?? when Python convert it into...(******)   Human.processing(Kiran)  -- Is is like this??? # this conversion is only for Object Method.
# no need of Kiran to store, there is no need to pass anything into it. 

# Using Classname, I am calling the Static Method.
Human.processing()  # It is a Static Method.

# Human.processing(Kiran) -- Error 
Human.processing() # This one is fine, since static method is not taking any argument. it takes no argument. 
    
    
    
print(dir(Human))

'''

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eye', 'feelings', 'nose', 'processing']

'''