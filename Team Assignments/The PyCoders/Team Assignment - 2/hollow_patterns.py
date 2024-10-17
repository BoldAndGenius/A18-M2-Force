'''
Hollow Square

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

n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()











'''
Hollow Plus

          *           
          *           
          *           
          *           
          *           
* * * * * * * * * * * 
          *           
          *           
          *           
          *           
          *   

'''

n = int(input()) # 11
for row in range(n):
    for col in range(n):
        if row==n//2 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    












'''
Hollow Multiply 


*                   * 
  *               *   
    *           *     
      *       *       
        *   *         
          *           
        *   *         
      *       *       
    *           *     
  *               *   
*                   * 

'''


n = int(input())  # 11
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    

'''
Hollow Minus 

                      
                      
                      
                      
                      
* * * * * * * * * * * 
                      
                      
                      
                      
                      


'''

n = int(input()) # 11
for row in range(n):
    for col in range(n):
        if row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    

'''
Hollow True Division 

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
*                    

'''

n = int(input()) # 11
for row in range(n):
    for col in range(n):
        if row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    



'''
Hollow Floor Division 

                  *   
                *   * 
              *   *   
            *   *     
          *   *       
        *   *         
      *   *           
    *   *             
  *   *               
*   *                 
  *                   

'''

n = int(input())
for row in range(n):
    for col in range(n):
        if row+col == n-2  or row+col ==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




# n = 5
# for row in range(n):
#     for col in range(n):
#         print((row,col),end=" ")
#     print()
# therefore relation is -  (r+c == n-2) or (r+c == n)









'''
Hollow Square Diagonal Cross

* * * * * * * * * * * 
* *               * * 
*   *           *   * 
*     *       *     * 
*       *   *       * 
*         *         * 
*       *   *       * 
*     *       *     * 
*   *           *   * 
* *               * * 
* * * * * * * * * * * 

'''

n = int(input()) # 11
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row+col==n-1 or row ==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    



'''
Hollow Right Triangle 

*                     
* *                   
*   *                 
*     *               
*       *             
*         *           
*           *         
*             *       
*               *     
*                 *   
* * * * * * * * * * * 

'''

n = int(input())  # 11
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
'''
Hollow Inverted Right Triangle 

* * * * * * * * * * * 
*                 *   
*               *     
*             *       
*           *         
*         *           
*       *             
*     *               
*   *                 
* *                   
*                     

'''

n = int(input()) # 11
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
    
    
    
    
    



'''
Square

* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * 

'''

n = int(input())
for row in range(n):
    for col in range(n):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
  
'''
Hollow Parallellogram

           * * * * * * * * * * * 
          * *               * * 
         *   *           *   * 
        *     *       *     * 
       *       *   *       * 
      *         *         * 
     *       *   *       * 
    *     *       *     * 
   *   *           *   * 
  * *               * * 
 * * * * * * * * * * * 

'''

n = int(input())  # 11
for row in range(n):
  print(" "*(n-row-1),end=" ")
  for col in range(n):
    if row==0 or row==n-1 or col==0 or col==n-1 or row==col or row+col==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
    
    
    
    
    
    
    
    
    
  
  
  
'''
Square Parallel Bar Pattern 

*       * 
*       * 
*       * 
*       * 
*       * 

'''
n = int(input())
for row in range(n):
  for col in range(n):
    if col==0 or col==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
'''
Hollow Hill Pattern 
[Practice]

          * 
        *   * 
      *       * 
    *           * 
  * * * * * * * * * 


'''


# First make the solid hill pattern, and the improvise to hollow.
n = int(input())
for row in range(n):
  for col in range(row,n):
    print(" ",end=" ")
  for col in range(row):
    if col==0 or row==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for col in range(row+1):
    if row==col or row==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
  
  
  
  
  
  










'''

Hollow Diamond 

        * *       
      *     *     
    *         *   
  *             * 
*                 * 
  *             *   
    *         *     
      *     *       
        * *         

'''

  
  
n = int(input())
for row in range(n-1):
  for col in range(n):
    if col+row==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for col in range(n-1):
    if row==col:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
for row in range(n):
  for col in range(n):
    if row==col:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for col in range(n):
    if row+col==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
  
  
  
  















# Hollow Diamond