

list = [1,2, 4.5, "kiran", "kajal"] 

#1 .append() 
# -- Take the value, and add the element at the end. 
# -- Return Type is None. Take argument. 

list.append("Pankaj")  # permanently it gets added into the list at the end. 
print(list) # [1, 2, 4.5, 'kiran', 'kajal', 'Pankaj', 'Pankaj']

#2 .copy() - Copy of the same list, store it. 

new_list = list.copy()
print(new_list) # [1, 2, 4.5, 'kiran', 'kajal', 'Pankaj', 'Pankaj']


#3 .clear() - remove/clear all the elements in a list.

list.clear()
print(list) # []


#4. .count() - count the number of occurences of an element. It return None.

mylist = [1, 23.4, 'kiran', True, 'kiran']
print(mylist.count('kiran'))  # 2 


#5 .remove()  - remove the 1st occurence of an element. 

mylist = [1, 23.4, 'kiran', True, 'kiran']
mylist.remove('kiran')
print(mylist)  # [1, 23.4, True, 'kiran']




# 6. 



print(dir(str))


'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'''

def func():
    print("hi")
    
class demo:
    # method 
    def func():
        print("hi")
    pass 


class str:
    def upper():
        
    def __upper__()


print(type(demo))



class demo:
    def kiran():
        print("Kiran")
    print("Kiran")

print(dir(demo))
'''

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'kiran']

'''


obj = demo()
print(type(demo))
print(dir(demo))

'''

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


'''


class Pyspider:
    var = 20 
    def myfunc(self,name):
        # print(name)
        # print(self.name)
        self.name = name 
        
obj = Pyspider() # od = {}
print(Pyspider.__dict__)
obj.myfunc("kiran")
print(obj.__dict__)


'''
{'__module__': 'builtins', 'var': 20, 'myfunc': <function Pyspider.myfunc at 0x00000238827A3100>, '__dict__': <attribute '__dict__' of 'Pyspider' objects>, '__weakref__': <attribute '__weakref__' of 'Pyspider' objects>, '__doc__': None}

'''

'''
{'__module__': 'builtins', 'var': 20, 'myfunc': <function Pyspider.myfunc at 0x00000238827A2DE0>, '__dict__': <attribute '__dict__' of 'Pyspider' objects>, '__weakref__': <attribute '__weakref__' of 'Pyspider' objects>, '__doc__': None}
'''





class Pyspider:
    var = 10 
    def myfunc2(self,name):
        print(name, "superclass")
class Jspider(Pyspider):
    var = 100 
    # def myfunc2(self,name):
    #     print(name)

obj = Jspider() 
# print(Jspider.__dict__)  
print(dir(Jspider))
print(obj.var)
obj.myfunc2("kiran")




'''

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'myfun', 'myfunc2', 'var']
'''

   
print(obj.var)

# what is super 




# multi level inheritnace 


class Pyspider:
    var = 10 
    def myfunc2(self,name):
        print(name, "superclass")
class Jspider(Pyspider):
    var = 100 
    def myfunc2(self,name):
        print(name)
class Qspider(Jspider):
    var = 200 
    def myfunc2(self,name):
        print(name)
obj = Qspider()
print(obj.var)  # 200 
obj.myfunc2("Faizan")
print(super(Qspider,obj).var)

print(super(super(Qspider,obj).var), obj).var))


var = 6 
var = 10 
print(super().var) # RuntimeError: super(): no arguments
print(super(var).var)





# Multiple Inheritance 

class FlyingAnimal:
    def fly(self):
        print("This animal can fly.")
class AquaticAnimal:
    def swim(self):
        print("This animal can swim.")
class Duck(FlyingAnimal, AquaticAnimal):
    def quack(self):
        print("This animal can quack.")
        
        
duck = Duck()
# using this duck object, I can call the function of it's Superclass.
duck.quack()  # from Duck Class 
duck.swim()
duck.fly()

# output -
'''
This animal can quack.
This animal can swim.
This animal can fly.
'''