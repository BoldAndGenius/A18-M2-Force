

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
                    #  Where Kiran gets stored ?? when Python convert it into...(******)   Human.processing(Kiran)  -- Is is like this???


# Using Classname, I am calling the Static Method.
Human.processing()  # It is a Static Method.

# Human.processing(Kiran) -- Error 
Human.processing() # This one is fine, since static method is not taking any argument. it takes no argument. 
    
    
    
    