# Collection is Homogenous or Not

collection = eval(input("Enter a Collection : "))  # [1,2]  # {1,2}
homogenous = True
# logic is  -- compare the data type of all elements from the data type of 1st element
first_element = type(collection[0])
for item in collection:
    if type(item) != first_element:
        homogenous = False 
if homogenous == True:
    print("Homogenous Collection")
else:
    print("Heterogenous Collection")



# Given Number is Prime or Not 

number = int(input("Enter a Number : "))
if number == 1:
    print("Not a Prime Number, Please enter number greater than 1")
elif number == 2:
    print("Prime Number")
else:
    prime = True
    for num in range(2,number):
        if number % num == 0:
            prime = False
            break
    if prime == True:
        print("Number is Prime")
    else:
        print("Number is Not a Prime")
