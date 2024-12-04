

# Magic Methods -- These are the special methods, which have some fixed functionality.
#               -- Magic Methods are also called "Dunder Method" (short for double underscore).
#               -- It starts with double underscore and ends with double underscore.
#               -- 
# Magic methods, also known as dunder methods (short for "double underscore"), 
# are special methods in Python that start and end with double underscores (e.g., __init__, __str__, __add__).

# They enable you to define custom behaviors for built-in Python operations, 
# such as object initialization, addition, string representation, comparisons, and more.




class Human:
    eyes = 2 
    nose = 1
    # __init__   - Constructor- To store object properties at the time of object creation.
    # Every time we create an object, it gets called once. 
    def __init__(self,name):
        self.name = name 
    # object is converted to a string 
    # return it, and then print it.
    def __str__(self):
        return "Object Instance"
    
obj = Human('Kiran')
print(obj)  # Object Instance 
# Earlier it was coming -  <Human object at 0x0000020AEE8CB6E0>
# Now, becuase of __str__  - String Representation - When we print the object, a message gets printed. 



    
    
class Sum:
    pass
    
# to see all the magic methods -- use dir()
print(dir(Sum))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
obj1 = Sum()
obj2 = Sum()
# print(obj1 + obj2) -- it will give error.
# to perform object addition, use __add__


class Sum:
    def __sum__(self):
        return "Addition"
    
    # to get the lenght of object
    def __len__(self):
        return 2
obj1 = Sum()
obj2 = Sum()
# print(obj1 + obj2)
print(len(obj1))



'''


List of Other Magic Methods -

Arithmetic Operations:
__sub__: Subtraction (-)
__mul__: Multiplication (*)
__truediv__: Division (/)
__floordiv__: Floor division (//)
__mod__: Modulus (%)
__pow__: Power (**)

Comparison Operations:
__lt__: Less than (<)
__le__: Less than or equal (<=)
__gt__: Greater than (>)
__ge__: Greater than or equal (>=)

Container Methods:
__contains__: in operator.

Custom Iteration:
__iter__: Returns an iterator.
__next__: Defines iteration behavior.



Why Use Magic Methods?

1. To integrate custom classes with Python's built-in operators and functions.

2. To enhance readability and maintainability by defining behavior inline with Python's idioms.

3. To make objects more versatile and reusable.

4. By implementing magic methods, you can design classes that feel intuitive and integrate seamlessly with Python's language features.


'''