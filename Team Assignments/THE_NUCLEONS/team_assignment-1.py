'''
"""
(Swastik)
        *       * * * * *
        * *     * * * *
        * * *   * * *
        * * * * * *
        * * * * * * * * *
              * * * * * *
            * * *   * * *
          * * * *     * *
        * * * * *       *
"""
n = int(input("enter a number :"))
for row in range(n):
    for col in range(n):
        if (row >= col and row <= n//2) or (row + col >= n-1 and col <= n//2) or (row <= col and row >= n//2) or (row + col <= n-1 and col >= n//2 ):
            print("*",end = " ")
        else:
            print(" ",end = " ")    
    print() 

"""
(Reverse Pyramid)
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *  
""""
n = int(input("enter the number : "))
for row in range(n):
    for col in range(n):
        if row <= col and row + col <= n-1:
            print("*",end = " ")
        else:
            print (" ",end = " ")
    print()   

"""
(Sand Glass)
        * * * * * * *
          * * * * *
            * * *
              *
            * * *
          * * * * *
        * * * * * * *
"""  
n = int(input("enter the number : "))
for row in range(n):
    for col in range(n):
        if (row <= col and row + col <= n-1) or (row >= col and row + col >= n-1):
            print("*",end = " ")
        else :
            print(" ",end = " ")
    print()   

"""
        ()
        * * * * * *
        * * * * *
        * * * *
        * * *
        * * * *
        * * * * *
        * * * * * *
"""
n = int(input("enter a number :"))
for row in range (n):
    for col in range(n):
        if row + col >= n-1 and row <= col:
            print (" ",end = " ")
        else :
            print("*",end = " ")    
    print()    
    
"""
        (Solid L)
        * * *
        * * *
        * * *
        * * *
        * * * * * * *
        * * * * * * *
        * * * * * * *
"""
n = int(input("enter a num :"))
for row in range (n):
    for col in range(n):
        if col <= (n//2)-1 or row >= (n//2)+1:
            print("*",end = " ")
        else :
            print(" ",end = " ")
    print()  
    
"""
        ()
        * * * * * * *
        * * * * * *
        * * * * *
        * * * * * * *
        * * * * * * *
        * * * * * * *
        * * * * * * *
"""   

n = int(input("enter a number : "))
for row in range(n):
    for col in range(n):
        if row + col <= n-1 or row >= n//2:
            print("*",end = " ")
        else :
            print(" ",end = " ")
    print()   

"""
      (Checkboard) 
        * * * * *
         * * * *
        * * * * *
         * * * *
        * * * * *
         * * * *
        * * * * * 
"""
n = int(input("enter a number : "))
for row in range(n):
    for col in range(n):
        if (row % 2 == 1 and col == 0) or (col == n-1 and col % 2 == 1):
            print(" ",end = " ")
        print("*",end = " ")
    print()
    '''
"""
    * * * * * * * * * 
      * * * * * * *   
        * * * * *     
          * * *       
            *
          * * *       
        * * * * *     
      * * * * * * *   
    * * * * * * * * *
"""
n=int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if (row<=col and row+col<=n-1) or (row>=col and row+col>=n-1) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
"""
n=int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        
            print("*", end=" ")
            
    print()

"""
      *
      * *
      * * *
      * * * *
      * * * * *
      * * * *
      * * *
      * *
      *
"""
n=int(input("enter number:"))
for row in range (n):
    for col in range (n):
        if  col==0 or (row==n//2 and col==n//2) or (row>=col and row<=n//2) or (row+col<=n-1 and row>=n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
                * 
              * * 
            * * * 
          * * * * 
        * * * * * 
          * * * * 
            * * * 
              * * 
                *  
"""

n=int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if col==n-1 or (row==col and col>=n//2) or (row+col==n-1 and col>=n//2) or (col>row and row+col>=n-1) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()