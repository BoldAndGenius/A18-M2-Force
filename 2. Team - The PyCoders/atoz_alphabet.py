'''

Team - The PyCoders 

Team Leader - Er. Kiran Kumar

Team Members Name -

1.
2.
3.
4.


'''

'''

A to Z Alphabet Pattern Printing

'''






'''


* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 



'''


n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
'''

* * * * * * * 
*           * 
*           * 
* * * * * * * 
*           * 
*           * 
* * * * * * * 


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n-1 or (col==n-1 and row<=n/2) or row==n//2 or (col==n-1 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    




  




'''

* * * * * * * * * * 
*                   
*                   
*                   
*                   
*                   
*                   
*                   
*                   
* * * * * * * * * * 


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()













'''

* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * * 



'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n-1 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            










