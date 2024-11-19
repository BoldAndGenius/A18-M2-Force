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



