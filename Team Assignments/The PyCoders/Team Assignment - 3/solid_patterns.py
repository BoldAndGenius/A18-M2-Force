
'''
Left Aligned Right Angle Triangle
or
Increasing Triangle Pattern

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 

'''

n = int(input())  # 11
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()
    
    
    
    
    




'''
Left Aligned Inverted Right Angle Triangle
or
Decreasing Triangle Pattern

* * * * * * * * * * * 
* * * * * * * * * * 
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

n = int(input())
for row in range(n):
    for col in range(row,n):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    



'''
Right Aligned Right Angle Triangle 
or
Right Sided Triangle 

                      * 
                    * * 
                  * * * 
                * * * * 
              * * * * * 
            * * * * * * 
          * * * * * * * 
        * * * * * * * * 
      * * * * * * * * * 
    * * * * * * * * * * 
  * * * * * * * * * * * 

'''
n = int(input())  # 10
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
        
        
        
        
        
        
        
        
        
    
    
'''

Right Aligned Inverted Right Angle Triangle


  * * * * * * * * * * * 
    * * * * * * * * * * 
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
n = int(input()) # 11
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Hill Pattern 

                      * 
                    * * * 
                  * * * * * 
                * * * * * * * 
              * * * * * * * * * 
            * * * * * * * * * * * 
          * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * * * 


'''

n = int(input()) 
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print("*",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()











'''
Reverse Hill Pattern 

  * * * * * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * 
          * * * * * * * * * * * * * 
            * * * * * * * * * * * 
              * * * * * * * * * 
                * * * * * * * 
                  * * * * * 
                    * * * 
                      * 



'''

n = int(input())  # 11
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print("*",end=" ")
    for col in range(row,n):
        print("*",end=" ")
    print()











'''
Diamond Pattern 

                      * 
                    * * * 
                  * * * * * 
                * * * * * * * 
              * * * * * * * * * 
            * * * * * * * * * * * 
          * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * 
          * * * * * * * * * * * * * 
            * * * * * * * * * * * 
              * * * * * * * * * 
                * * * * * * * 
                  * * * * * 
                    * * * 
                      * 



'''


n = int(input())  # 11
for row in range(n-1):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print("*",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print("*",end=" ")
    for col in range(row,n):
        print("*",end=" ")
    print()
        












    
    


'''
Pyramid 

                      * 
                    * * * 
                  * * * * * 
                * * * * * * * 
              * * * * * * * * * 
            * * * * * * * * * * * 
          * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * * *



'''

n = int(input())  # 11
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print("*",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
    

# Pyramid & Hill Pattern -- Both are same! 
# Reverse Pyramid & Reverse Hill Pattern -- Both are same! 











'''
Double Hill Pattern 

                      *                                         * 
                    * * *                                     * * * 
                  * * * * *                                 * * * * * 
                * * * * * * *                             * * * * * * * 
              * * * * * * * * *                         * * * * * * * * * 
            * * * * * * * * * * *                     * * * * * * * * * * * 
          * * * * * * * * * * * * *                 * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * *             * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * *         * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * *     * * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 


'''

n = int(input())  # 11
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print("*",end=" ")
    for col in range(row+1):
        print("*",end=" ")
        
    for col in range(row,n-1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print(" ",end=" ")
        
    for col in range(row):
        print("*",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Butterfly 

(Good Question to Practice)


*                     * 
* *                 * * 
* * *             * * * 
* * * *         * * * * 
* * * * *     * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * *     * * * * * 
* * * *         * * * * 
* * *             * * * 
* *                 * * 
*                     * 


'''

n = int(input())  # 11

for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
        
    for col in range(row,n-1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print(" ",end=" ")
         
    for col in range(row+1):
        print("*",end=" ")
    print()
    
for row in range(n):
    for col in range(row,n):
        print("*",end=" ")
    for col in range(row):
        print(" ",end=" ")
    for col in range(row):
        print(" ",end=" ")
    for col in range(row,n):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



'''
Sandglass Pattern

* * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * 
        * * * * * * * * * * * 
          * * * * * * * * * 
            * * * * * * * 
              * * * * * 
                * * * 
                  * 
                  * 
                * * * 
              * * * * * 
            * * * * * * * 
          * * * * * * * * * 
        * * * * * * * * * * * 
      * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * 


'''

n = int(input())  # 11
for row in range(n):
    for col in range(row):
        print(" ",end=" ")
    for col in range(row,n-1):
        print("*",end=" ")
    for col in range(row,n):
        print("*",end=" ")
    print()
# n = int(input())  # 11
for row in range(n):
    for col in range(row,n-1):
        print(" ",end=" ")
    for col in range(row):
        print("*",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Left Pascal's Triangle Pattern

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


'''

n = int(input())
for row in range(n-1):
    for col in range(row+1):
        print("*",end=" ")
    print()
for row in range(n):
    for col in range(row,n):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Right Pascal's Triangle 


              * 
            * * 
          * * * 
        * * * * 
      * * * * * 
    * * * * * * 
  * * * * * * * 
    * * * * * * 
      * * * * * 
        * * * * 
          * * * 
            * * 
              * 



'''
n = int(input())  # 11
for row in range(n-1):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n):
        print("*",end=" ")
    print()