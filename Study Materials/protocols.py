##########################################################################
'''magic methods'''
from random import seed
#__call__ -> executed when you try to call an object
#__repr__ or __str__ -> executed when you try to print an object
#__contains__ -> executed when you try to use membership operator on an object
#__getitem__ -> executed when you try to index an object
#__setitem__ -> executed when you try to assign a value to an indexed object
#__getattribute__ -> executed when . operator is used on object to access an attribute
#__getattr__ -> executed when . operator is used on object to access an attribute
#__setattr__ -> executed when . operator is used on object to modify an attribute
#__delattr__ -> executed when del keyword is used on an object attribute
#__gt__ -> executed when '>' is used between two objects
#__ge__ -> executed when '>=' is used between two objects
#__lt__ -> executed when '<' is used between two objects
#__le__ -> executed when '<=' is used between two objects
#__eq__ -> executed when '==' is used between two objects
#__ne__ -> executed when '!=' is used between two objects

#------------------------------------------------------------------------
class Sample:
    var1 = 10
    var2 = 20
    var3 = 30
    
    # def __init__(self, a):
    #     self.a = a

    @staticmethod
    def method1():
        '''this is an example of static method'''
        print("in method1")

    def __call__(self):
        print("i made the object a callable")

    def __str__(self):
        return "hello"

    def __repr__(self):
        return '10'

    def __contains__(self, value):
        return value in Sample.__dict__.values()
    
    def __getitem__(self, index):
        if index == 1:
            return self.var1
        elif index == 2:
            return self.var2
        elif index == 3:
            return self.var3
        else:
            return "index out of range"
    
    def __setitem__(self, index, value):
        if index == 1:
            Sample.var1 = value
        elif index == 2:
            Sample.var2 = value
        elif index == 3:
            Sample.var3 = value
        else:
           print("index not present")
    
    def __getattribute__(self, name):
        print("go home")

    def __setattr__(self, name, value):
        print("go home again")

    def __gt__(self, address):
        return self.a > address.a
    
    def __ge__(self, address):
        return self.a >= address.a

    def __lt__(self, address):
        return self.a < address.a

    def __le__(self, address):
        return self.a <= address.a

    def __eq__(self, address):
        return self.a == address.a

    def __ne__(self, address):
        return self.a != address.a


s1 = Sample()
s1.a = 20
# print(callable(s1))
# s1()            #s1.__call__()          #Sample.__call__(s1)
# print(s1)       #s1.__str__()           #Sample.__str__(s1)
# print(40 in s1) #s1.__contains__(40)    #Sample.__contains__(40)
# print(s1[5])    #s1.__getitem__(5)      #Sample.__getitem__(5)

# s2 = Sample(20)
# print(s1 > s2)     #s1.__gt__(s2)      #Sample.__gt__(s1, s2)

# s1[5] = 15         #s1.__setitem__(5, 15)       #Sample.__setitem__(s1, 5, 15)
# print(Sample.__doc__)
# print(s1.method1.__doc__)

###################################################################
'''----if __name__ == '__main__'----'''
#to check if the given function or class is called in the same module in which it is defined
#this random function will be executed in this module
#if it is used in other module, 'if' block will not be executed
def random():
    if __name__ == '__main__':
        print(__name__)
        print("nonsense")

# random()

#--------------------------------------------------------------------
class Simple:
    def __init__(self):
        if __name__ == '__main__':
            print("object created")
        else:
            raise NameError


# s1 = Simple()


##########################################################################

class Some:
    a = 10
    b = 20
    def __init__(self):
        self.p = 100
        self.q = 200

    def __setattr__(self, name, value):
        if name == 'a':
            Some.b = value
        elif name == 'b':
            Some.a = value
        else:
            print("nahi chalega")
        
    def __delattr__(self, name):
        raise NameError

Some.c = 50
s1 = Some()
s1.b = 30           #Some.__setattr__(s1, 'b', 30)
print(s1.b)
# del s1.r
# print(s1.p)

##########################################################################