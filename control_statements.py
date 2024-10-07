#There are 3 loop control statements
#1.break
#2.continue
#3.pass

#1.wap to check if the collection is homogeneous collection or not --(ASHA S)
collection = eval(input("Enter a collection :"))
homogeneous = True
type_ref = type(collection[0])
for item in collection:
    if type(item) != type_ref:
        homogeneous = False
        break
if homogeneous == True:
    print(f"{collection} is homogeneous collection")
else:
    print(f"{collection} is heterogeneous collection")

#2.wap to check if the given number is prime or not --(ASHA S)
num = int(input('Enter a number :'))
if num==1:
    print(f"{num} is not a prime")
elif num==2:
    print(f"{num} is  a prime")
else:
    prime=True
    for _num in range(2,num):
        if num%_num==0:
            prime=False
            break
if prime==True:
    print(f"{num} is  a prime")
else:
    print(f"{num} is not a prime")

#3.wap to validate usrename and password using while loop and for loop --(ASHA S)
actual_username=input('Enter username :')
actual_password=input('Enter password :')
while True:
    username=input('Enter username :')
    if username==actual_username:
        break
for _ in range (3):
    password=input("Enter password :")
    if password==actual_password:
        break
else:
    print('user blocked...')


#4.wap to check if the string consists only lowercase letters --(ASHA S)
string=input("Enter a string :")
lower=True
for char in string:
    if char.islower()!=True:
        lower=False
        break
if lower==True:
    print(f"{string} contains only lowercase characters")
else:
    print(f"{string} contains otherthan lowercase characters")

#5.wap to check if the number consists only digits
num=input('Enter a number :')
number=True
for digit in num:
    if digit.isnumeric()!=True:
        number=False
        break
if number==True:
    print(f"{num} contains only digits...")
else:
    print(f"{num} contains otherthan digits...")

#6.wap to check if the string consists only alphabets --(ASHA S)
string=input("Enter a string :")
alpha=True
for char in string:
    if char.isalpha()!=True:
        alpha=False
        break
if alpha==True:
    print(f"{string} contains only alphabets")
else:
    print(f"{string} contains otherthan alphabets")

#7.wap to check if the string consists only uppercase letters --(ASHA S)
string=input("Enter a string :")
upper=True
for char in string:
    if char.isupper()!=True:
        upper=False
        break
if upper==True:
    print(f"{string} contains only uppercase letters")
else:
    print(f"{string} contains otherthan uppercase letters")
