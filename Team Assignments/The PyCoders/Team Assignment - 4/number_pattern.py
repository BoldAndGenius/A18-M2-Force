'''
Number Pattern - 1 : Repeat Value 1 

1 
1 1 
1 1 1 
1 1 1 1 
1 1 1 1 1 
1 1 1 1 1 1 
1 1 1 1 1 1 1 


'''

n = int(input()) # 7
for row in range(n):
    for col in range(row+1):
        print("1",end=" ")
    print()
    
    
    
    
    
    
    


'''
Number Pattern - 2 : Repeat Value 1 in Inverted Left Aligned Right Angle Triangle 

1 1 1 1 1 1 1 
1 1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 
1 1 1 
1 1 
1 


'''


n = int(input())  # 7
for row in range(n):
    for col in range(row,n):
        print("1",end=" ")
    print()








'''
Number Pattern - 3 : Repeat Value 1 in Right Aligned Right Angle Triangle 

              1 
            1 1 
          1 1 1 
        1 1 1 1 
      1 1 1 1 1 
    1 1 1 1 1 1 
  1 1 1 1 1 1 1 


'''

n = int(input())  # 7
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row+1):
        print("1",end=" ")
    print()
    
    
    
    
    
    
    


'''
Number Pattern - 4 : Repeat Value 1 in Right Aligned Inverted Right Angle Triangle

  1 1 1 1 1 1 1 
    1 1 1 1 1 1 
      1 1 1 1 1 
        1 1 1 1 
          1 1 1 
            1 1 
              1 
'''

n = int(input()) # 7
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n):
        print("1",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Number Pattern - 5 : Repeat Value 1 in Hill Pattern 

              1 
            1 1 1 
          1 1 1 1 1 
        1 1 1 1 1 1 1 
      1 1 1 1 1 1 1 1 1 
    1 1 1 1 1 1 1 1 1 1 1 
  1 1 1 1 1 1 1 1 1 1 1 1 1 
  
  
'''

n = int(input())
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print("1",end=" ")
    for col in range(row+1):
        print("1",end=" ")
    print()
    
    
    
    
    
    
'''
Number Pattern - 6 : Repeat Value 1 in Reverse Hill Pattern

  1 1 1 1 1 1 1 1 1 1 1 1 1 
    1 1 1 1 1 1 1 1 1 1 1 
      1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 
          1 1 1 1 1 
            1 1 1 
              1 
              
'''

n = int(input())  # 7
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print("1",end=" ")
    for col in range(row,n):
        print("1",end=" ")
    print()
    
    
    
    
    
    
    
    
    


