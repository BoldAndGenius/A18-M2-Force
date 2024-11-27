

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