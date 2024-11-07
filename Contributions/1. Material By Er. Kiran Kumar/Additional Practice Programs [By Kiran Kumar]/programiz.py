# 600 Questions 



'''
Write a function to convert a given string to title case .

input = "hello world"
output = "Hello World"
'''


# Using Without Function
# use the title function

input = "hello world"
output = input.title()
print(output)


# Using Functions

def title_case(input):
    output = input.title()
    return output
input = "hello world"
print(title_case(input))

















'''

Write a function to swap two given integers 

for this input - 
3
4

the result should be -
(4,3)


'''


# without function

num1 = 3
num2 = 4

num1,num2 = num2,num1 
print(f"({num1},{num2})")


# with function

def swap_numbers(num1,num2):
    num1, num2 = num2,num1 
    return (num1,num2)
print(swap_numbers(1,2))