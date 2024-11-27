# Quiz - 1 {Wonderful Question to get deeper into OOPS}



class Point:
    var = 10 
    def method(self, address):
        print(self.var , address.var)

class Joint: 
    var = 100 
    def method(self, address):
        address.method(self)

p1 = Point()
j1 = Joint()


# At the time of Object Creation -- the object dicionaty & class dictionary
print(Point.__dict__)
# {'__module__': 'builtins', 'var': 10, 'method': <function Point.method at 0x000001A121022D40>, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}

print(p1.__dict__)  # {}
print(j1.__dict__) # {}

j1.method(p1) # can be written as ------------ Joint.method(j1,p1) --- method(self, address) -- so, self is j1, address is p1
             # further it gets calculated to --   address.method(self) --- p1.method(j1) ---- it can be further write as ........   Point.method(p1,j1) -- p1 is self, j1 is address
             # self.var --- p1.var --- 10
             # address.var ------ j1.var ---100 
             
# Output -   
# 10 
# 100 





# Quiz - 2 {Wonderful Question to get deeper into OOPS}

# confuser question 

class Point:
    var = 10 
    def myfunc1(self):
        print("I am the best!")
class Joint:
    var = 100 
    def myfunc1(self):
        print("I am the greatest person ever born on this planet.")
    def confuser(self, address):
        address.confuser = address.myfunc1 
        address.myfunc1 = self.myfunc1 

print(Point.__dict__) # {'__module__': 'builtins', 'var': 10, 'myfunc1': <function Point.myfunc1 at 0x00000212A4362DE0>, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}

print(Joint.__dict__)  # {'__module__': 'builtins', 'var': 100, 'myfunc1': <function Joint.myfunc1 at 0x00000212A4363060>, 'confuser': <function Joint.confuser at 0x00000212A4363100>, '__dict__': <attribute '__dict__' of 'Joint' objects>, '__weakref__': <attribute '__weakref__' of 'Joint' objects>, '__doc__': None}


# after object creation 
p1 = Point()
j1 = Joint()
print(p1.__dict__) # {}
print(j1.__dict__) # {}

j1.confuser(p1)  # Joint.confuser(j1,p1) # so self is j1, address is p1. 
# address.confuser = address.myfunc1   =>   p1.confuser = p1.myfunc1  => in Point's Object Dictionary....there is no confuser key, so it will create confuser key..........and value will be p1.myfunc1  ---- so inside Point class, for myfunc1 the value will be "Point's myfunc1 address"
# so for confuser key, the address of Point's myfunc1 will be stored 

p1.myfunc1() #  I am the best!
# p1.confuser() # check in object dictionary of Point (since p1 is the object of Point class).............. so in object dictionary...for confuser key...it is storing the address of address of Point's myfunc1 

Point.myfunc1(p1)


# How   
# I am the greatest person ever born on this planet.
# I am the best!



class Point:
    var = 10 
    def myfunc1(self):
        print("I am the best!")
class Joint:
    var = 100 
    def myfunc1(self):
        print("I am the greatest person ever born on this planet.")
    def confuser(self, address):
        address.confuser = address.myfunc1 
        address.myfunc1 = self.myfunc1 

print(Point.__dict__)
print(Joint.__dict__) 
p1 = Point()
j1 = Joint()
print(p1.__dict__)
print(j1.__dict__)
j1.confuser(p1) 
p1.myfunc1()