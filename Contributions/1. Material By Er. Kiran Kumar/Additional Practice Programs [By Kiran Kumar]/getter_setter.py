# Constructor  -- at the time of object creation only, I can store the object properties in the object dictionary. 
# Everytime we create an object, automatically the constructor gets called once 
# __init__ magic method is called a Constuctor.
# The arguments taken by __init__ magic method is, we need to pass at the time of class calling. 

class MyConstructor:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def new_func(self):
        pass 
obj = MyConstructor("Kiran",23)
print(obj.name) # Kiran
print(obj.age) # 23 
# to see the object dictionary
print(obj.__dict__)  # object dictionary =>  {'name': 'Kiran', 'age': 23}
print(MyConstructor.__dict__) # class dicionary => {'__module__': 'builtins', '__init__': <function MyConstructor.__init__ at 0x00000254FFB636A0>, 'new_func': <function MyConstructor.new_func at 0x00000254FFB63880>, '__dict__': <attribute '__dict__' of 'MyConstructor' objects>, '__weakref__': <attribute '__weakref__' of 'MyConstructor' objects>, '__doc__': None}










# Access Modifier in OOPs 

class PersonalLife:
    __pin = "2323@" # private variable 
    def my_pin(self):  # getter
        return PersonalLife.__pin
    def update_mypin(self,new_pin): # setter
        self.__pin = new_pin # assign the new pin 
        return self.__pin # now call that new pin
Kiran = PersonalLife()
print(Kiran.my_pin())  # 2323@ 

print(Kiran.update_mypin('@#$%^')) # @#$%^
print(Kiran._PersonalLife__pin)  # @#$%^