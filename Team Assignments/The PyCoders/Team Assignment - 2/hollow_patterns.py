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
    