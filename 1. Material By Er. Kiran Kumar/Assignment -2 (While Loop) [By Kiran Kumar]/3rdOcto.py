

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
            
            
# Simple Right-Angled Triangle:
''' 

*
**
***
****
*****

'''

for i in range(1,6):
    print("*"*i)
    
    
    
# Inverted Right-Angled Triangle Pattern

'''

*****
****
***
**
*

'''

for i in range(5,0,-1):
    print(i*"*")
    
    
# Pyramid Pattern

''' 

    *
   ***
  *****
 *******
*********


'''


'''
Right-Angled Triangle with Numbers:

1
12
123
1234
12345



Floyd’s Triangle

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15


Alternating 0 and 1 Triangle

1
01
101
0101
10101



Hollow Square

*****
*   *
*   *
*   *
*****



Pascal's Triangle


      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1



Alphabet Pyramid

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA


'''

# Print All Keywords

import keyword
print(keyword.kwlist)


# Print All Softkeywords

import keyword
print(keyword.softkwlist)

#output - ['_', 'case', 'match', 'type']