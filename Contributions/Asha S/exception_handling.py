''' Exception Handling'''

# Default Exception Handling
"""1. wap to checks a person eligible to vote or not using exception handling"""
try:
    age=int(input('Enter your age :'))
except:
    print("Enter valid age...")
else:
    if age>=18:
        print('You are eligible to vote.....')
    else:
        print('You are not eligible to vote.....')

####################################################################################################

"""2. wap to handle a ZeroDevisionError exception when dividing a number by zero"""
try:
    num1=int(input('Enter num1 :'))
    num2=int(input('Enter num2 :'))
    res=num1/num2
except:
    print('Enter valid number....')
else:
    print(f"Result :{res}")

####################################################################################################

"""3. wap that executes an operation on a list and handles an IndexError exception if index out of range"""
collection=[10.20,30,24,89,10]
try:
    index=int(input('Enter index value :'))
    Element_at_index=collection[index]
except:
    print('Enter a valid index')
else:
    print(f"Element present at index {index} is {Element_at_index}")

####################################################################################################

"""4. wap to print factorial of a number by taking input from user using exception handling"""
try:
    num=int(input('Enter a number :'))
except:
    print('Enter a valid number....')
else:
    if num>0:
        factorial=1
        for factor in range(1,num+1):
            factorial*=factor
        print(f"Factorial of {num} is {factorial}")
    else:
        print('Enter a +ve number.....')
        
####################################################################################################

# Generic Exception Handling   

""" 1. wap which takes dictionary and key as a input if key is present in dictionary print value associated with that key using generic exception handling """
try:
    collection=eval(input('Enter a dictionary :'))
    key=eval(input("Enter a key :"))
    value=collection[key]
except Exception as error_msg:
    print(error_msg)
else:
    print(f"value asssociated with {key} is {value}")
finally:
    print('Execution ends here...')

""" 2.wap to add two number, 
if sum is even check for a pallindrome
if sum is odd print sum  using generic exception handling"""
try:
    num1=int(input('Enter num1 :'))
    num2=int(input('Enter num2 :'))
except Exception as msg:
    print(msg)
else:
    res=num1+num2
    temp=res
    if res%2==0:
        rev=0
        while res!=0:
            last_digit=res%10
            rev=rev*10+last_digit
            res//=10
        if rev==temp:
            print(f"Even sum of {num1} and {num2} is => {temp}\nreverse of {temp} is {rev} \n {temp} is pallindrome number..")
        else:
            print(f'Even sum of {num1} and {num2} is => {temp}\nreverse of {temp} is {rev}\n{temp} is not pallindrome number..')
    else:
        print(f'Sum of {num1},{num2}  =>{temp}')

"""3. wap to handle program from raising an exception for printing factorial of a number"""
try:
    num=int(input('Enter a number :'))
except Exception as err_msg:
    print(err_msg)
else:
    fact=1
    if num==0:
        print(f"Factorial of {num} is {fact} ")
    else:
        for factor in range(1,num+1):
            fact*=factor
        print(f'Factorial of {num} is {fact}')

