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


