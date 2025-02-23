

# Polymorphism - Many Faces --- Based on the cirumstances, the Operator/Functios/Methods behanve differently. 

# 1. Compile Time Polymorphism --- 1. Method Overloading     2. Operator Oerloading.
# 2. Run Time Polymorphism ------- 1. Method Overriding. 



# Example of Method Overloading. 


def sum(num1,num2):
    print(num1 + num2)
def sum(num1, num2 ,num3):
    print(num1 + num2 + num3)
def sum(num1, num2, num3,num4):
    print(num1,num2,num3,num4)

# now the updated sum function is, def sum(num1, num2, num3,num4):  ...as all the above functions get overridded..
    
# sum(10,20)  #gets error
# sum(10,20,30)  #gets error

sum(10,20,30,40)  # this will give value...because after overridden, the current function is the 3rd one having 4 arguments. 



# So, in Python...Method Overloading not possible, instead it do Overridding! Values get updated! 





# Example of Operator Overloading 

print(2+2) # 4     # Here plus operator is working as a summation on integer data type.
print('2'+'2') # '22'    # Here plus is working as a concatenation on string data type.







# Example of Method Overriding 

class Cat:
    def __init__(self,name):
        self.name = name 
    def sound(self):
        print(f"{self.name} is meow....")
    def walk(self):
        print(f"{self.name} is walking...")

class Dog(Cat):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print(f"{self.name} is barking...")
    def running(self):
        print(f"{self.name} is runnig...")

cat1 = Cat("mycat")
cat1.sound()
cat1.walk()
        
dog1 = Dog('mydog')
dog1.sound()  # Dog Class is already inheriting the sound() function from the Cat class, but that function got overidde to it's own function sound.   --- This is called Method Overriding.

dog1.running()


