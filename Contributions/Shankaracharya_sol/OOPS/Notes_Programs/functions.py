#WAP to define a function which adds two numbers and print the same.
def add(num1: int | float, num2 :int | float):  #function defintion
    return num1 + num2
print(add(14,558))     #function call

#WAP to define a function which asks for username and password and print the same.
def credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(f"Your username is:{username}")
    print(f"Your password is:{password}")
credentials()

#WAP to define a function which returns the sqaure of a number if it is even else cube of it.
def square_cube(num: int | float):
    if num % 2 == 0:
        print("The num is even")
        return (num ** 2)
    else:
        print("The num is odd")
        return (num ** 3)
print(square_cube(int(input("Enter any num:"))))

#WAP to define a function which returns the last element of a collection.
def last_element(collection: str | list | tuple):
    return collection[-1]
print(last_element(eval(input("Enter a collection:"))))


#WAP to define a function which displays the multiplication table of a number.
def multiplication_table(num : int):
    for fact in range(1,11):
       print(f"{num} x {fact} = {num * fact}")
multiplication_table(int(input("Enter a num:")))

#WAP to define a function which displays all the vowels in a given string.
def display_vowels(string : str):
    output = ""
    for char in string:
        if char in "aeiouAEIOU":
            output += char
    return output
print(display_vowels(input("Enter a string:")))

