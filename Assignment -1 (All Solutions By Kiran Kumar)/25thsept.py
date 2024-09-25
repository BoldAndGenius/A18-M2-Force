# Nested If

# Question - 81
# Write a program to create an Instagram login page.

# let's assume, credentials of instagram login is =>   username = kiran     password = 1234

username = input("Enter Your Username :")
password = input("Enter Your Password :")
if (username == "kiran") and (password == '1234'):
    print("Login Successfully")
else:
    print("Invalid Credentials")






# Question - 82
# Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3




# heterogenous_tuple = (1, True, 2+7j, [1,2,3] {1,2,3})


collection = ( 1, True, 2+6j , [1,2,3], {1,2,3} )
middle_value = collection[len(collection) // 2] 
# print(middle_value)  #  # 2+7j  [Just for validation]
if type(middle_value) == str:
    if len(middle_value) > 3:
        print(middle_value)
 
 
#  for this collection -  ( 1, True, "kiran", [1,2,3], {1,2,3} )   - it gonna print the string
  








# Question - 83
# Write a program.To check the greater among four numbers using nested if.


num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))
num3 = int(input("Enter the number 3 :"))
num4 = int(input("Enter the number 4 :"))

if (num1 > num2) and (num1> num3) and (num1>num4):
    print(f"{num1} is Greatest.")
elif (num2>num1) and (num2>num3) and (num2>num4):
    print(f"{num2} is Greatest.")
elif (num3>num1) and (num3>num2) and (num3>num4):
    print(f"{num3} is Greatest.")
elif (num4>num1) and (num4>num2) and (num4>num3):
    print(f"{num4} is Greatest.")
elif (num1 == num2 == num3 == num4):
    print("All numbers are Equal.")
else:
    print("Invalid")
    

