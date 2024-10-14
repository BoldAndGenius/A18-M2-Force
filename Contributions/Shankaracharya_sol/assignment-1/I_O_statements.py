#Write a program to print the square of a given integer number.
num = int(input("Enter any integer:"))
square = num ** 2
print(square)

#Write a program to find the product of two float numbers.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
product = num1 * num2
print(product)

#Write a program to find the area of a rectangle.
length = eval(input("Enter the length of the rectangle:"))
breadth = eval(input("Enter the breadth of the rectangle:"))
area = length * breadth     #perimeter = 2 * (length + breadth)
print(area)

#Write a program to reverse the given string.
string = input("Enter a string:")
reverse = string[:2:-1]        #[start:stop:step]
print(reverse)

#Write a Program to find the sum, difference, product and division.Between 2 integer numbers.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
floor_division = num1 // num2
print(sum,difference,product,division,floor_division)

#Write a program to find the simple interest.
principal_amount=eval(input("Enter your initial amount:"))
rate = eval(input("Enter rate of interest:"))
time = eval(input("Enter the duration in years:"))
simple_interest = (principal_amount * rate * time) / 100
print(simple_interest)

#Write a program to calculate area of triangle
base = eval(input("Enter the base of the traingle:"))
perpendicular_height = eval(input("Enter the perpendicular height of the traingle:"))
area = (1/2) * base * perpendicular_height
print(area)

#Write a Python code to swap two variables.
variable1 = eval(input("Enter value for variable1:"))
variable2 = eval(input("Enter another value for variable2:"))
swap = variable1
variable1 = variable2
variable2 = swap
print(f"variable1:{variable1}")
print(f"variable2:{variable2}")

#Write a Python program to calculate the square root of a given number
num = eval(input("Enter a number:"))
sqaure_root = num ** (1/2)
print(sqaure_root) 

#Write a Python program to find the area of a circle.
radius = eval(input("Enter the radius of the circle:"))
area = (22/7) * radius ** 2
print(area)