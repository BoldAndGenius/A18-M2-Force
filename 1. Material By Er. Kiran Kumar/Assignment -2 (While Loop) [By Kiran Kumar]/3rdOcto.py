

# Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.



# Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)



# Q18. Write a program to add first n terms of the following series using a while loop: 1/1! + 1/2! + 1/3! + …….. + 1/n!






# Q19. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.

    



# Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered.




# Diagonal Pattern 

for row in range(5):
    for column in range(5):
        if row == column:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    

# 1st Row Pattern
for row in range(1):
    for column in range(5):
        print("*", end=" ")
        
# 2nd Row Pattern
for row in range(2):
    for column in range(5):
        if row == 0:
            print("", end="\n")
            break
        else:
            print("*", end=" ")
            

# 3rd Row Pattern 
for row in range(3):
    for column in range(5):
        if row in [0,1]:
            print("", end="\n")
            break
        else:
            print("*", end=" ")
            
# 1st Column Pattern 
for row in range(5):
    for column in range(1):
        if column == 0:
            print("*", end="\n")
        
# 2nd Column Pattern 
for row in range(5):
    for column in range(2):
        if column == 1:
            print(" ",end=" ")
            print("*",end="\n")
            


# 3rd Column Pattern 
for row in range(5):
    for column in range(5):
        if column == 2:
            print(" ",end=" ")
            print(" ", end= " ")
            print("*", end="\n")