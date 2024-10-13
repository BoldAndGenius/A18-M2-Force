
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