
# Object Methods - self is used as the first argument.
#                - Can only be accessed through object only. 
#                - No Decorator is required.



class Human:
    eyes = 2 
    ears = 2
    def __init__(self, name):
        self.name = name 
        
    # object method -- self is used as a first argument, no decorator is there. Can Only be accessed by the Object.
    def processing(self):
        print(f'{self.name} is processing')
    
 
# Using Object I am calling the Object Method.   
Kiran = Human('Kiran')
Kiran.processing() # Kiran is processing
#Python converts to like this --  Human.processing(Kiran)


# Using Class I am trying to call the Object Method.
# Human.processing()  - get error
# TypeError: Human.processing() missing 1 required positional argument: 'self'


        