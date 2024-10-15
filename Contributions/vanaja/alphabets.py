#letter A
n=5
for row in range(n):
    for col in range(n):
        if (col==0 or col==n-1 )and row!=0 or row==0 and col!=0 and col!=n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter B
n=5
for row in range(n):
    for col in range(n):
        if col==0 or (row==0 or row==n//2 or row==n-1) and col!=n-1 or (col==n-1 and row!=0 and row!=n//2 and row!=n-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# letter C
n=5
for row in range(n):
    for col in range(n):
        if (row==0 or row==n-1 )and col!=0 or(col==0 and row!=0 and row!=n-1 )  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter D
n=5
for row in range(n):
    for col in range(n):
        if col==0 or (row==0 or row==n-1 )and col!=n-1 or( col==n-1) and row!=0 and row!=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter E
n=5
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2 or row==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

 #letter F
n=5
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter G
n=5
for row in range(n):
    for col in range(n):
        if ((row==0 or row==n-1) and col!=0) or(col==0 and row!=0 and row!=n-1) or (col==n-1 and row>=n//2) or (row == n//2 and col >= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# letter H
# n=5
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
 
#letter I
# n=5
for row in range(n):
    for col in range(n):
        if row==n-1 or row==0 or col==n//2  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter J
n=5
for row in range(n):
    for col in range(n):
        if  row==0 or col==n//2 or (col==0 and row>n//2 ) or (row==n-1 and col<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter K
n=5
for row in range(n):
    for col in range(n):
        if col==0 or (row+col==n-2 and row<=n//2) or(col==row-1 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter L
n=5
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter M
n=5
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or( (row+col==n-1 or row==col) and row<=n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter N
n=5
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or col==row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter O
n=5
for row in range(n):
    for col in range(n):
        if ((row==0 or row==n-1)and col!=0 and col!=n-1) or ((col==0 or col==n-1)and row!=0 and row!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter P
n=5
for row in range(n):
    for col in range(n):
        if col==0 or ((row==0 or row==n//2 )and col!=n-1)or (col==n-1 and row==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#letter Q
n=5
for row in range(n):
    for col in range(n):
        if ((row==0 or row==n-1)and col!=0 and col!=n-1) or ((col==0 or col==n-1)and row!=0 and row!=n-1)or (row==col and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter R
n=5
for row in range(n):
    for col in range(n):
        if col==0 or ((row==0 or row==n//2 )and col!=n-1)or (col==n-1 and row==1)or col==row and col>=n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter S
n=5
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0) or( row==n-1 and col!=n-1) or  row==n//2 or (row==1 and col==0)or (row==n-2 and col==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter T
n=5
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter U
n=5
for row in range(n):
    for col in range(n):
        if ((col==0 or col==n-1)and row!=n-1) or ((row==n-1)and col!=0 and col!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



# letter W
n=5
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or( (row+col==n-1 or row==col) and row>=n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter X
n=5
for row in range(n):
    for col in range(n):
        if col==row or col+row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter Y
n=5
for row in range(n):
    for col in range(n):
        if row+col==n-1 or (row==col and row<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter Z
n=5
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

