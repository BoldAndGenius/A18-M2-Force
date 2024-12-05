# class Sample:
#     var = 10

#     @staticmethod
#     def method1(self):
#         print("in method1")
# print(callable(Sample))         # True
# s1 =  Sample()
# print(callable(s1))             # False
# print(s1)                       # <__main__.Sample object at 0x000001EE80535F10>
# print(s1[0])                      # TypeError: 'Sample' object is not subscriptable

from typing import Any


class Sample:
    # var1 = 10
    # var2 = 40
    def __init__(self,num):
        self.num = num

    # def __init__(self,num):
    #     self.num = num
    # @staticmethod
    # def method1(self):
    #     print("in method1")

    # def __call__(self):
    #     print("i made this callable")

    # def __str__(self):
    #     return "dirty fellow this is an object of sample class"
    # def __repr__(self):
    #     return "both are same"
    
    # def __contains__(self,value):
    #     return value in Sample.__dict__.values()     #to get the values of the dictionary in form of list
    
    # def __getitem__(self,index):
    #     if index == 1:
    #         return self.var1
    #     elif index == 2:
    #         return self.var2
    #     else:
    #         return "index out of range"
        
    # def __gt__(self,address):
    #     return self.num > address.num
    
    # def __ge__(self,address):
    #     return self.num >= address.num
    
    # def __lt__(self,address):
    #     return self.num < address.num
    
    # def __le__(self,address):
    #     return self.num <= address.num
    
    # def __ne__(self,address):
    #     return self.num != address.num
    
    # def __eq__(self,address):
    #     return self.num == address.num
    
    # def __setitem__(self,index,value):
    #     if index == 1:
    #         Sample.var1 = value
    #     elif index == 2:
    #         Sample.var2 = value
    #     elif index == 3:
    #         Sample.var3 = value
    #     else:
    #         # Sample.var[index] = value
    #         print("hello")
    # def __getattribute__(self, name: str) -> Any:
    #     print("go home")
    # def __setattr__(self, name: str, value: Any) -> None:
    #     print("go home man")
    def __add__(self,address):
        return self.num + address.num
    def __sub__(self,address):
        return self.num - address.num
    def __mul__(self,address):
        return self.num * address.num
    def __truediv__(self,address):
        return self.num / address.num
    def __floordiv__(self,address):
        return self.num // address.num
    def __mid__(self,address):
        return self.num % address.num
    def __pow__(self,address):
        return self.num ** address.num
    def __iadd__(self,address):
        return self.num + address.num
    def __isub__(self,address):
        return self.num + address.num
    def __imul__(self,address):
        return self.num + address.num
    def __itruediv__(self,address):
        return self.num + address.num
    def __ifloor__(self,address):
        return self.num + address.num
    def __iadd__(self,address):
        return self.num + address.num
    def __and__(self,address):
        return self.num & address.num
    def __or__(self,address):
        return self.num | address.num
    def __xor__(self,address):
        return self.num ^ address.num
    def __invert__(self):
        return ~self.num
    def __lshift__(self,address):
        return self.num << address.num
    def __rshift__(self,address):
        return self.num >> address.num
v1 = Sample(10)
v2 = Sample(40)
print(~v1)
# print(dir(Sample))
# s1 = Sample()
# s1.var                              # go home
# s1.var1 = 30                        # go home man

# print(callable(Sample))             # True
# s1 =  Sample(10)
# s2 = Sample(20)
# print(callable(s1))               # True
# print(s1)                         # dirty fellow this is an object of sample class

# print(100 in s1)                  # False
# print(10 in s1)                   # True

# print(s1[1])                      # 10
# print(s1[2])                      # 40
# print(s1[5])                      # index out of range


# print(s1 > s2)

# s1[4] = 15
# print(s1[4])

# print(s1.__doc__)               # it will give the intro written in docs string about class or a function
# print(Sample.__module__)        # it will give the location of the file (__main__)
# print(s1.__sizeof__())          # it will give the size of an object in bytes
# print(s1[1].__sizeof__()) 
# print(s1[2].__sizeof__()) 