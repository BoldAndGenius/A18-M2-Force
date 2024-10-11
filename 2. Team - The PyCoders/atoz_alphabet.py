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
A Alphabet


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

B Alphabet

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
C Alphabet

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

D Alphabet

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
            













'''
E Alphabet

* * * * * * * * * * * 
*                     
*                     
*                     
*                     
* * * * * * * * * * * 
*                     
*                     
*                     
*                     
* * * * * * * * * * * 


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    


'''

F Alphabet


* * * * * * * * * * 
*                   
*                   
*                   
*                   
* * * * * * * * * * 
*                   
*                   
*                   
*     


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
G Alphabet

* * * * * * * * * * 
*                   
*                   
*                   
*                   
*         * * * * * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * * 


'''

n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or (col==n-1 and row>n//2) or (row==n//2 and col>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    










'''
H Alphabet


*                 * 
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
n = int(input()) #10
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()













'''
I Alphabet

* * * * * * * * * * * 
          *           
          *           
          *           
          *           
          *           
          *           
          *           
          *           
          *           
* * * * * * * * * * * 


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


'''
J Alphabet

* * * * * * * * * * * 
          *           
          *           
          *           
          *           
          *           
          *           
          *           
          *           
          *           
* * * * * *   

'''

n = int(input()) # 11
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or (row==n-1 and col<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
K Alphabet


*                   * 
*                 *   
*               *     
*             *       
*           *         
*         *           
*           *         
*             *       
*               *     
*                 *   
*                   * 


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or (row==col and row>=n//2) or (row+col==n-1 and row<=n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    





'''
L Aphabet


*                     
*                     
*                     
*                     
*                     
*                     
*                     
*                     
*                     
*                     
* * * * * * * * * * * 

'''

n = int(input())  # 11
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    





'''
M Alphabet

*                   * 
* *               * * 
*   *           *   * 
*     *       *     * 
*       *   *       * 
*         *         * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 


'''

n = int(input())  # 10
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and col<=n//2) or (row+col==n-1 and col>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    


'''
N Alphabet

*                   * 
* *                 * 
*   *               * 
*     *             * 
*       *           * 
*         *         * 
*           *       * 
*             *     * 
*               *   * 
*                 * * 
*                   * 



'''

n = int(input())  # 11
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    




'''
O Alphabet

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

n = int(input()) #10
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==0 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()