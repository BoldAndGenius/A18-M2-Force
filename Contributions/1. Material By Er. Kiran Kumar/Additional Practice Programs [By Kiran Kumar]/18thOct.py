

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