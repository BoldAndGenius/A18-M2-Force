
# Frequently Asked Python Program 

# Question Number - Swap 2 Numbers 

# Approach -1 
# By Using Temporary Variable 

num1 = 10 
num2 = 20 
print("Before Swapping",num1, num2)

temp = num1 
num1 = num2 
num2 = temp 

print("After Swapping",num1, num2)


# Approach - 2
# Without Temporary Variable 

num1 = 10 
num2 = 20 
print("Before Swapping",num1, num2)

num1,num2 = num2,num1 

print("After Swapping",num1, num2)