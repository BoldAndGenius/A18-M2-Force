#WAP to check if a collection is a homogeneous collection or not.
collection = eval(input("Enter a collection:"))
ref = collection[0]
for item in range(1,len(collection)):
    if type(ref) != type(item):
        print("collection is not homogeneous")
        break
else:           #this else block will only work if all the iterations of for loop completed
                #if in b/w iterations if break throws out of the loop then this else block will not get execeuted bcz of partial iterations.
    print("collection is homogeneous")

#WAP to check if a given number is prime or not.

number = int(input("Enter a number:"))
prime = True
if number == 1:
    print("not prime")
elif number == 2:
    print("prime")
else:
    for i in range(2,number):
        if number % i == 0:
            prime = False
            break
    print(prime)

#WAP to validate a username & password using while loop and for loop.
actual_username = "raishan_____"
actual_password = "Shan@123"
while True:
    username = input("Enter your username:")
    if username == actual_username:
        break
for i in range(3):
    password = input("Enter your password:")
    if password == actual_password:
        print("logged in successfully")
else:
    print("Account blocked due to 3 wrong attempts")

#WAP to check if the string consists of only lowercase:
string = input("Enter a string:")
lowercase = True
for char in string:
    if not('a' <= char <= 'z'):
        lowercase =  False
        break
print(lowercase)

#WAP to print even number using loop.
for num in range(101):
    if num % 2 == 1:
        continue
    else:
        print(num)

#WAP to extract all integer values from a given list
list_ = eval(input("Enter a list:"))
integer = []
for item in list_:
    if type(item) != int:
        continue
    else:
        integer.append(item)
print(integer)

#WAP to find the count of similar character present in two string based on index.
string1 = input("Enter string1:")
string2 = input("Enter string2:")
count =0
for index in range(len(string1)):
    if string1[index] != string2[index]:
        continue
    else:
        count += 1
print(count)

#Program to understand difference b/w pass and continue

for num in range(5):
    if num % 2 == 1:
        continue
        print("skipping odd",end=" ") #it will not executed
for num in range(5):
    if num % 2 == 1:
        pass
        print("skipping odd")           #it will executed