
# 1. HALLOW SQUARE QUADS.
n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        #if row==0 or col==0 or row==n//2 or col==n//2 or row==n-1 or col==n-1:
        if (row and col)==0 or row==n//2 or col==n//2 or row==n-1 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    


# output
'''

* * * * * * * * * 
*       *       * 
*       *       * 
*       *       * 
* * * * * * * * * 
*       *       * 
*       *       * 
*       *       * 
* * * * * * * * *       '''



# 2.HALLOW PENTAGON

n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        if row==n-1 or (col==0 and row>=n//2) or (col==n-1 and row>=n//2) or (row+col==n//2) or col-row==n//2  :
        #if row==n-1 or ((col==0 or col==n-1) and row>=n//2) or (row+col==n//2) or col-row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")

# Output
'''
        *
      *   *       
    *       *     
  *           *   
*               *
*               *
*               *
*               *
* * * * * * * * *       '''




# 3.HALLOW LEFT BLOCK

n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or (row==0 and col<=n//2)  or (col==n//2 and row<=n//2) or (row==n//2 and col>=n//2) or (col==n-1 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

# Output
'''

* * * *
*     *
*     *
*     * * * *
*           *
*           *
* * * * * * *       '''

                                 

# 4.HALLOW STAR.

n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        if row==n//2 or col==n//2 or (col==0 and row<=n//2) or (row==0 and col>=n//2) or (col==n-1 and row>=n//2) or (row==n-1 and col<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

# output

'''
*     * * * * 
*     *
*     *
* * * * * * *
      *     *
      *     *
* * * *     *                '''


# 5. HALLOW PLUS PATTERN

n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        if  row==n//2 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

# Output

'''
      *
      *
      *
* * * * * * *
      *
      *
      *           '''


                       

#6.SQUARE DIAGONAL CROSS.

n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        if  row==0 or col==0 or row==n-1 or col==n-1 or row+col==n-1 or row==col:
        #if (row and col)==0 or row==n-1 or col==n-1 or row+col==n-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# Output
'''

* * * * * * * * * 
* *           * *
*   *       *   *
*     *   *     *
*       *       *
*     *   *     *
*   *       *   *
* *           * *
* * * * * * * * *       '''
    

#  7. HALLOW ZIGZAG PATTERN

n=int(input("enter the number :"))
repetitions = 3
for _ in range(repetitions):
    for row in range(n):
        for col in range(n):
            if row == 0  or row + col == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  
      
# Output
'''

* * * * * 
      *
    *
  *
*
* * * * *
      *
    *
  *
*
* * * * *
      *
    *
  *
*                  '''


# 8. HALLOW STAR SHAPE PATTERN.

n=int(input("enter the number :"))
for row in range(n):
    for col in range(n):
        if  row==n//2 or col==n//2 or row==col or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

# Output
'''

*     *     * 
  *   *   *
    * * *
* * * * * * *
    * * *
  *   *   *
*     *     *             

 '''




# 9. HALLOW ARROW PATTERN

n=9
for row in range(n):
    for col in range(n):
        if (col==n//2 and row>=n//2) or  (row==n-1 and col==n//2)  or (row==n//2 and col<=n//2 ) or (row==n//2 and col>=4) or (row+col==n//2 and row<=n//2)  or  (col-row==n//2 and row<=n//2)  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

#Output
'''

         *
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
        *
        *
        *
        *            

'''



# 10.HALLOW FLAG.
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0   or row==n//3 or row==n-3 or (col==n-1 and row<=n-3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# output
'''

* * * * * * * * * 
*               * 
*               * 
* * * * * * * * * 
*               * 
*               *
* * * * * * * * *
*
*
 
'''

  

#11.HOLLOW KITE.
n = int(input("enter a number:"))

for row in range(n):
    for col in range(n):
        if (col == n // 2 or               
            row == n // 2 or               
            (row + col == n // 2 and row <= n // 2) or  
            (col - row == n // 2 and row <= n // 2) or  
            (row - col == n // 2 and row >= n // 2) or  
            (row + col == (n // 2) + (n - 1) and row >= n // 2)):  
            print('*', end='')
        else:
            print(' ', end='')
    print()


'''
output:
     *     
    ***    
   * * *
  *  *  *
 *   *   *
***********
 *   *   *
  *  *  *
   * * *
    ***
     *
'''


#12.HOLLOW RHOMBUS.
n = int(input("enter a number:"))

for row in range(n):
    print('  ' * (n - row - 1), end='')
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:  
            print('*', end=' ')
        else:
            print(' ', end=' ')  
    
    print() 

'''
output:
          * * * * * *
        *         *
      *         *
    *         *
  *         *
* * * * * *
'''




#13.HOLLOW BUTTERFLY.
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if ( col == 0 or col == n - 1 or 
            row == 0 or row == n - 1 or 
        row == col or row + col == n - 1):
            print('*', end='')
    else:
        print(' ', end='')
    print()

'''
output:
***********
**       **
* *     * *
*  *   *  *
*   * *   *
*    *    *
*   * *   *
*  *   *  *
* *     * *
**       **
***********
'''





#14. Hollow Left Angle Triangle Pattern
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if col == 0 or row == n - 1 or row == col:
            print('*', end='')
        else:
            print(' ', end='')
    print()


'''
output:
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
*        *
***********
'''

#15.HOLLOW HOURGLASS.
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if row == 0 or row==col or row+col == n-1 or row==n-1 :       
            print('*', end='')
        else:
            print(' ', end='')
    print()

'''
output:

***********
 *       * 
  *     *
   *   *
    * *
     *
    * *
   *   *
  *     *
 *       *
***********
'''



#16.HOLLOW PRYAMID.

n = int(input("enter a number:"))
for row in range(n):
    for col in range(2 * n - 1):  
        if   row+col==n-1 or  row == n - 1 or col == n - 1 + row:
            print('*', end='')
        else:
            print(' ', end='')  
    print()

'''
output:
    *    
   * *   
  *   *
 *     *
*********
'''


#17.HOLLOW CROSS.
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if col==row or col+row==n-1:
            print('*', end='')
        else:
            print(' ', end='') 
    print() 


'''
output:
*     *
 *   * 
  * *
   *
  * *
 *   *
*     * 
'''



#18.HOLLOW INVERTED TRIANGLE.
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or (col==n-1 and row>=n//2) or (row==n//2 and col>=n//2) or (col+row==n-1  and row<=n//2):
            print('*', end='')
        else:
            print(' ', end='')
    print()

'''
output:
***********
*        * 
*       *
*      *
*     *
*    ******
*         *
*         *
*         *
*         *
***********

'''


#19.DIAGONAL SPLIT HEXAGON.
n = int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if row==0  or row==n-1  or (row+col==n//2 or row-col==n//2)  :   
            print('*', end='')
        else:
            print('   ', end='')
    print()


'''
output:
*******
      *
   *
*
   *
      *
*******
'''





# 20. HALLOW SQUARE
n=int(input("enter the no:"))
for row in range (n):
    for col in range (n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

# OUTPUT:
'''
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * *    
    
'''


#21. HALLOW RIGHT TRIANGLE
n=int(input("enter the no:"))
for row in range (n):
    for col in range (n):
        if col==0 or row==n-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 


 # OUTPUT:
'''
*
* *       
*   *     
*     *   
* * * * *     '''            



# 22. HALLOW INVERTED RIGHT TRIANGLE
n=int(input("enter the no:"))
for row in range (n):
    for col in range (n):
        if row==0 or col==0 or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

# OUTPUT:
'''
* * * * * 
*     *   
*   *     
* *       
*
'''



# 23.DIAMOND
n=int(input("enter the no:")) 
for row in range(n):
    for col in range(n):
        if (row+col==n//2) or (col-row==n//2) or (row-col==n//2) or (row+col==n+(n//2)-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# OUTPUT:
'''
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
'''    




# 24.HALLOW RECTANGLE
n = 5
m = 11
for row in range(n):
    for col in range(m):
        if row==0 or row==n-1 or col==0 or col==m-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# OUTPUT:
''' 
    * * * * * * * * * *
    *                 *
    *                 *
    *                 *
    * * * * * * * * * *    
''' 





#  25.HALLOW HOUSE
n=9
for row in range (n):
    for col in range (n):
        if row==4 or row+col==4 or col-row==4 or (col==2 and row>=5) or (col==6 and row>=5) or (row==n-1 and col>=2 and col<=6) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   

# OUPUT:
'''
        *
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
    *       *     
    *       *     
    *       *     
    * * * * *   
'''    





#  26.PARALLELOGRAM
n=int(input("enter the no:"))
for row in range(n):
    print(" " * (n-row-1),end="")
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row+col==n-1 or row==col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# OUTPUT:
'''
      * * * * * * * 
     * *       * *
    *   *   *   *
   *     *     *
  *   *   *   *
 * *       * *
* * * * * * *
'''    






