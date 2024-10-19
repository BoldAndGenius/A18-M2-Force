

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






# Function - Group of statements that will do some particular task 

# Average of 3 Numbers Using Function

def avg(num1,num2,num3):   # function definition
    average = (num1+num2+num3)/3
    return average
result1=avg(10,20,30)  # function calling
result2=avg(5,10,20)
print(result1)
print(result2)

'''
Output -
20.0
11.666666666666666
'''


# The parameter that are used in function definition are called Formal Parameters. The parameter that are used in function call are called Actual Parameters. 

# Value Returning Function -- Any function that returns some value. 
# Non Value Returning Function -- Any function that returns nothing.  No value.



# Non value Returning Function
def display_message():
    print("Hello")
    print("How, are you?")
display_message()

'''
output -
Hello
How, are you?
'''






# Formal Parameters & Actual Parameters can be same or different. 
         # default parameter   n3 = 0
def average(n1,n2,n3=0):  # formal parameter = n1,n2,n3
    avg = (n1+n2+n3)/3.0
    return avg 

print("Welcome")
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
num3 = int(input("Enter the Third Number : "))

# It is called Positional Arguments 
result = average(num1,num2,num3)  # actual parameter = num1,num2, num3
print(result)

# here formal parameter & actual parameter are different. No issues. 


# Keyword Argument 
result = average(n3 = 30, n1 = 50, n2 = 60) # value will assign based on the keyword, not based on the position. 
print(result)


# because of Default Argument for n3=0, only two arguments can work.
result = average(10,20)
print(result)










# Anonymous Function or Lambda Function 
# Function without any name 

sum = lambda num1,num2: num1+num2
print("sum is : ",sum(10,20))


# Output -
# sum is :  30





# Variable Length Arguments 
# It is beneficial when we don't know how many parameters need to mention while definiting the function. 

def func1(*mylist):  # use star
    for item in mylist:
        print(item)
    
func1(10,20)
func1(5)
func1(5,10,15,20)





# Local & Global Variable 

# Local Variable
def func1():
    n = 5  # local variable
    print("The value of n is",n)

def func2():
    n = 10  # local variable
    print("The value of n is",n)
    func1()

func2()

'''
Output -
The value of n is 10
The value of n is 5
'''










# Problem in Local Variable
# Got Error, since in func1, n is not defined. 

def func1():
    # n = 5  # local variable -- we commend it, hence get error. 
    print("The value of n is",n)

def func2():
    n = 10  # local variable - this value will only be used by this function, not any other function.
    print("The value of n is",n)
    func1()

func2()

# to solve the error, 









# Global Variable 

n = 10  # this is a global variabe, therefore can be used by any function

def func1():
    print(n)
def func2():
    print(n)
    func1()

func2()


'''
Output -

10
10
'''







n = 10  # this is a global variabe, therefore can be used by any function

def func1():
    print(n) # Here it will take from gloabal variable, therefore n = 10 will be considired
def func2():
    n = 20  # Local Variable -- Only applicable to the function 2
    print(n) # hence, here it will take n = 20 from the local variable.
    func1()

func2()


'''
Output -

20
10
'''









# Updating Global Variable in Function

# Here we will get the error 
num = 10
def func1():
    num = num + 1  # Here it is a local variable 
    # Whenever we try to update or modify the variable in a function, it will treat that variable as local variable. The solution for this problem is, We need to tell the Python that, it is a global variable not the local variable. 
    print("Variable value in func1 is",num)
func1()



# The remove the Error 
num = 10
def func1():
    global num   #We are telling to the python that, the num variable we are modiying or using in this func1 is a global variable. 
    num = num + 1
    print("The value of num in func1 is",num)

func1()

'''
Output -
The value of num in func1 is 11
'''