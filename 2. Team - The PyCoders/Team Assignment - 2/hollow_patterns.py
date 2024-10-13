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