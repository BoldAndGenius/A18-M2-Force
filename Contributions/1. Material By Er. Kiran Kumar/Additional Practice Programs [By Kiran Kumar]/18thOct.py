

# function taking function name as an argument (Program - 1)


# Each time you create a function, id has been assigned.
    # 0x1   # assign 0x2
def demo(func_name):
    print("In Demo")
     # assign 0x2 
    func_name()
    # 0x2
def sample():
    print("In Sample")

# 0x1 # 0x2
demo(sample)


# Output -
'''

In Demo
In Sample

'''









# function taking function name as an argument (Program - 2)

# Each time you create a function, id has been assigned.
  # 0x1  # 0x3 as been assigned
def demo(func):
    print("In Demo")
       # 0x2
    def inner():
        print("In Inner")
        func()
         
    return inner   # it will return 0x2 address tot the calling function
    # 0x3
def greet():
    print("Hello World") 

# 0x1 # 0x3
demo(greet)

'''
Output -

In Demo
'''







# Decorator 
# function taking function name as an argument (Program - 3)


# Each time you create a function, id has been assigned.
  # 0x1  # 0x3 as been assigned
def demo(func):
    print("In Demo")
       # 0x2
    def inner():
        print("In Inner")
        func()
         
    return inner   # it will return 0x2 address tot the calling function, means it will go to demo(greet). Therefore store to greet variable.
    # 0x3
def greet():
    print("Hello World") 

        # 0x1 # 0x3
greet = demo(greet)
# greet variable store the return inner -- hence 0x2 will be stored, hence it is the address of inner function, now you can call it
greet()   # therefore "In Inner" gonna print. And then it will call the func(), which has the address 0x3, which is the address of greet() function, hence the "Hello World" gets printed.


'''
Output -

In Demo
In Inner
Hello World

'''










# function taking function name as an argument (Program - 4)


# Each time you create a function, id has been assigned.

    # 0x1         #  0x4   0x2    0x3  has been assigned from the function call
def ambani_wedding(star1, star2, star3):
    print("Welcome to the Wedding")
    # 0x4 assigned from the parameter
    star1()
    # 0x2 assigned from the parameter
    star2()
    # 0x3 assigned from the parameter
    star3()
  # 0x2
def prabhas():
    print("Hello World")
  # 0x3
def rajni():
    print("Hello Logo")
  # 0x4
def yash():
    print("Hello Duniya")
    
  # 0x1     # 0x4  # 0x2  # 0x3
ambani_wedding(yash,prabhas,rajni)


'''
Output -
Welcome to the Wedding
Hello Duniya
Hello World
Hello Logo
'''






# Employee Info Function
def emp_info(name,age,salary):
    print(f"Employee Name -> {name}")
    print(f"Employee Age -> {age}")
    print(f"Employee Salary -> {salary}")

emp_info("Kiran",18, 400000000)





# Positional Arguments 
def add_and_concat(num1,num2,string1,string2):
    print(num1+num2)
    print(string1+string2)
add_and_concat(10,20,"Kiran","Kumar")

'''
Output -
30
KiranKumar
'''




# Default Arguments 
def add (num1, num2 = 0):
    sum = num1 + num2 
    print(sum)
add(10,20)
add(10)  # num2 will become 0  [no error]




# Keyword Argument 
def emp_info(name,age,salary):
    print(f"Employee Name -> {name}")
    print(f"Employee Age -> {age}")
    print(f"Employee Salary -> {salary}")

emp_info(age=18, name="Kiran", salary=400000000)


'''
Output -
Employee Name -> Kiran
Employee Age -> 18
Employee Salary -> 400000000

'''








# Average of 3 Numbers Using Function

def avg(num1,num2,num3):
    average = (num1+num2+num3)/3
    return average
result1=avg(10,20,30)
result2=avg(5,10,20)
print(result1)
print(result2)

'''
Output -
20.0
11.666666666666666
'''