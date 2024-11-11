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
"""for row in range(5):
    char = "A"
    for col in range(5):
        print(char,end = " ")
        char = chr(ord(char) + 1)
    print()
print()
char = "A"
for row in range(5):
    for col in range(5):
        print(char,end = " ")
    char = chr(ord(char) + 1)
    print()
print(sep=" ",end=" ")

char="A"
for row in range(5):
    for col in range(5):
        print(char,end = " ")
        char = chr(ord(char) + 1)
    print()
n = 5
char = "A"
for row in range(n):
    for col in range(n):
        print(char,end = " ")
        char = chr(ord(char) + 1)
    print()
    char = chr(ord(char) - (n-1) )

print()

n = 5
char = "A"
for row in range(n):
    new = char
    for col in range(n):
        print(new,end = " ")
        if col >= n // 2:
            new = chr(ord(new) - 1 )
        else:
            new = chr(ord(new) + 1)
    print()
    char = chr(ord(char) + 1)

'''
(Butterfly)
        *                   * 
        * *               * *
        * * *           * * *
        * * * *       * * * *
        * * * * *   * * * * *
        * * * * * * * * * * *
        * * * * *   * * * * *
        * * * *       * * * *
        * * *           * * *
        * *               * *
        *                   *
'''
n=11
for row in range(n):
    for col in range(n):
        if (col > row and row + col <= n-2) or (row > col and row + col >= n):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

    
n=5
for row in range(n):
    for col in range(n):
        if row == n-1 or col + row >= n-1:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
"""
'''
         0.2333335525
         .**   **
        * * * * *
        * * * * *
         * * * *
          * * *
            *

'''
list1=["hello",1,{2,3},1+2j]
item=list1[ -1: 0:-2]
print(item)