# Print R 


n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (col==n-1  and row<=n//2) or row==n//2 or (row==col and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    


# Print K

n = int(input())
for row in range(n):
    for col in range(n):
        if col==0 or (col+row==n-1 and row<=n//2) or (row==col and row>n//2) or (row==n//2 and col<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   
    

# Print V 

n = int(input())
for row in range(n):
    for col in range(n):
        if (row==col and col<=n//2) or (row+col==n-1 and col>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
# Solid Pattern -

''' 

*         
* *       
* * *     
* * * *   
* * * * * 

Left Aligned Triangle Pattern
'''

n = int(input())
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or row==col or row>col:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()


    