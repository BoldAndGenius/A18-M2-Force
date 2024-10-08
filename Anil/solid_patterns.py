n=int(input("Enter rows:"))


'''

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *

'''
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or row==col or row>col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()    


'''
* * * * * * * * *
  * * * * * * * *
    * * * * * * *
      * * * * * *
        * * * * *
          * * * *
            * * *
              * *
                *

'''
for row in range(n):
    for col in range(n):
        if col==n-1 or row==0 or row==col or row<col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()


'''

* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*

'''
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row+col==n-1 or row+col<=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()

'''
                *
              * *
            * * *
          * * * *
        * * * * *
      * * * * * *
    * * * * * * *
  * * * * * * * *
* * * * * * * * *

'''
for row in range(n):
    for col in range(n):
        if col==n-1 or row==n-1 or row+col==n-1 or row+col>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()

'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

'''
for row in range(n):
    for col in range(n):
        if row==0 or (row==col and row<=n//2) or (row+col==n-1 and row<=n//2) or (row<col and row+col<=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()


'''




        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

'''
for row in range(n):
    for col in range(n):
        if (row==col and row>=n//2) or (row+col==n-1 and row>=n//2) or (row>col and row+col>=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()


'''

* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *

'''
for row in range(n):
    for col in range(n):
        if row==0  or (row+col==n-1 and row<=n//2) or (row<col and row+col<=n-1) or col==0 or row==n-1 or row==col or  (row+col<=n-1) or row>=col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()


'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

'''
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1 or row==0 or row == n-1 or (row<col and row+col<=n-1) or (row>col and row+col>=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *

'''   
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or (row==0 and col<=n//2) or (col==n//2 and row<=n//2) or (row==n//2 and col>=n//2) or (col==n-1 and row>=n//2)  or col<=n//2 or row>=n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    
print()   

'''
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *

'''
for row in range(n):
    for col in range(n):
        if col==0 or  row==0 or (row+col==n-1 and row<=n//2) or (row==n//2 and col>=n//2) or (col==n-1 and row>=n//2) or row==n-1 or row>=n//2 or (row<col and row+col<=n-1) or col<=n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()