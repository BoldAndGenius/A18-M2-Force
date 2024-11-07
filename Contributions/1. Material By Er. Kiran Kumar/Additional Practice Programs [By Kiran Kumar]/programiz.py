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