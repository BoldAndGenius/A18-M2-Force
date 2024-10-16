n=7 #A
for row in range(n):
    for col in range(n):
        if (col==0 and row>n//2) or (col==n-1 and row>n//2) or row==n//2 or (row+col==n//2 ) or col-row==n//2 :
            print("*",end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7     #B
for row in range(n):
    for col in range(n):
        if col==0 or row==n//2 or (row==0 and col!=n-1) or (col==n-1 and row<n//2 and row!=0) or (row==n-1 and col!=n-1) or (col==n-1 and row>n//2 and row!=n-1):
            print("*",end=' ')
        else:
            print(' ', end=' ')
    print()
print()
n=7 #C
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0)  or (row==n-1 and col!=0) or (col==0 and row!=0 and row!=n-1):
            print("*",end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #D
for row in range(n):
    for col in range(n):
        if (row==0 and col!=n-1)  or (row==n-1 and col!=n-1) or (col==0 ) or (col==n-1 and row!=0 and row!=n-1)  :
            print("*",end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #E
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (row==n//2 and col<n-2) or row == n-1:
            print("*", end= ' ')
        else:
            print('', end=' ')
    print()
print()

n=7   #F
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (row==n//2 and col<n-2):
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #G
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0) or (col==0 and row!=0 and row!=n-1) or (row==n-1 and col!=0 and col!=n-1) or (col==n-1 and row>n//2 and row!=n-1)or (row==n//2 and col>n//2 ):
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #H
for row in range(n):
    for col in range(n):
        if col in (0,n-1) or row==n//2:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7   #I
for row in range(n):
    for col in range(n):
        if  row==0 or row==n-1 or col==n//2:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7  #J
for row in range(n):
    for col in range(n):
        if row==0 or (col==n//2 and row!=n-1 ) or (row==n-1 and col!=0  and col<n//2) or (row<n-1 and col<1 and row>n//2) :
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7   #K
for row in range(n):
    for col in range(n):
        if  col==1 or (row+col==n-1 and row<n//2) or (row==col and row>=n//2) or (row==n//2 and col<n//2 and col>0):
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7    #L
for row in range(n):
    for col in range(n):
        if  col==0 or row==n-1:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #M
for row in range(n):
    for col in range(n):
        if col==0 or col ==n-1 or (row==col and row<=n//2) or (row+col==n-1 and row<=n//2):
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #N
for row in range(n):
    for col in range(n):
        if  col==0 or col==n-1 or row==col:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #O
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0 and col!=n-1) or (row==n-1 and col!=0 and col!=n-1) or (col==0 and row!=0 and row!=n-1) or (col==n-1 and row!=0 and row!=n-1):
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()


n=7 #P
for row in range(n):
    for col in range(n):
        if (col==0 and row!=0) or (row==0 and col!=0 and col!=n-1) or (row==n//2 and col!=n-1) or (col==n-1 and row!=0 and  not row>=n//2) :
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7# Q
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0 and col!=n-1)  or (row==n-2 and col!=0 and col!=n-1)  or (col==0 and row!=0 and row<n-2 )or (col==n-1 and row!=0 and row!=n-2) :
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7    #R
for row in range(n):
    for col in range(n):
        if (col==0 and row!=0) or (row==0 and col!=n-1 and col!=0) or (col==n-1 and row!=0 and row<n//2) or (row==n//2 and col!=n-1) or (row>n//2 and row==col) :
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #S
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0) or (col==0 and row<n//2 and row!=0) or (row==n//2 and col!=0 and col!=n-1) or (col==n-1 and row>n//2 and row!=n-1) or (row==n-1 and col!=n-1 ) :
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #T

for row in range(n):
    for col in range(n):
        if row==0 or col==n//2:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #U
for row in range(n):
    for col in range(n):
        if (col==0 and row!=n-1)or (col==n-1 and row!=n-1) or (row==n-1 and col!=0 and col!=n-1):
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=13 #V
for row in range(n):
    for col in range(n):
        if  (row==col and row<=n//2)or (row+col==n-1 and row<n//2):
            print("*", end=' ')
        else:
            print(' ', end='')
    print()

n=7 #W
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and row>n//2) or ( row+col==n-1 and row>=n//2):
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #X
for row in range(n):
    for col in range(n):
        if  row+col==n-1 or row==col:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n=7 #Y
for row in range(n):
    for col in range(n):
        if (row==col and row<n//2) or (row+col==n-1 and row<n//2) or (col==n//2 and row>=n//2) :
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()
print()
n=7 #Z
for row in range(n):
    for col in range(n):
        if row==0 or row+col==n-1 or row==n-1:
            print("*" , end=' ')
        else:
            print(' ', end=' ')
    print()