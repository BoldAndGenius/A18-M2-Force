class NonSense:
    ...

    def angry(self):
        print("angry")
    
    def abuse(self):
        print("f*uck")

class Sense(NonSense):
    ...
    def Kind(self,name):
        self.name = name
        print("kind")
    
    def Intelligent(self):
        print("intelligent")
        
# print(NonSense.__dict__)
# print()
# print(Sense.__dict__)
# print(dir(Sense))
jwalini = Sense()
jwalini.Kind("jwalini")
print()
print(jwalini.__dict__)
print()
print(Sense.__dict__)
print()
print(NonSense.__dict__)