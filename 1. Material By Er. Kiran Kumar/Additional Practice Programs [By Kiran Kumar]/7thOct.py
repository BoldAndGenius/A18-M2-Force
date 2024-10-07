# 3*3 Matrix 

n = 3
for row in range(n):
    for col in range(n):
        print((row,col), end=" ")
    print()
    


# 10*10 Matrix

n = 10
for row in range(n):
    for col in range(n):
        print((row,col),end=" ")
    print()
    
    
# Print L 

n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0  or  row == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
# Print C 

n = int(input())
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
# Print O 

n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
# Print A 
n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

# Print I 

n = int(input())
for row in range(n):
    for col in range(n):
        if row == 0  or  row == n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
# Print F

n = int(input())
for row in range(n):
    for col in range(n):
        if row == 0  or  col == 0  or row == n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
