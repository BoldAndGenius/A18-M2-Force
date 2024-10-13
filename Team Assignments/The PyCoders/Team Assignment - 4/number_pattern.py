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
    
    
    
    
    
    
    
    
    


'''
Number Pattern - 7 : Repeat Value 1 in Diamond Pattern 

             1 
            1 1 1 
          1 1 1 1 1 
        1 1 1 1 1 1 1 
      1 1 1 1 1 1 1 1 1 
    1 1 1 1 1 1 1 1 1 1 1 
  1 1 1 1 1 1 1 1 1 1 1 1 1 
    1 1 1 1 1 1 1 1 1 1 1 
      1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 
          1 1 1 1 1 
            1 1 1 
              1 


'''

n = int(input())
for row in range(n-1):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print("1",end=" ")
    for col in range(row+1):
        print("1",end=" ")
    print()
# n = int(input())
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print("1",end=" ")
    for col in range(row,n):
        print("1",end=" ")
    print()
    
    
    
    
    
    
    
    
    


'''
Number Pattern - 8 : 1,22,333 in order for Left Aligned Right Angle Triangle

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 


'''

n = int(input())
num = 1
for row in range(n):
    for col in range(row+1):
        print(num,end=" ")
    num = num + 1 
    print()
    
        
        
        
        
        
        
        





'''
Number Pattern - 9 : 111,22,3 in order for Left Aligned Inverted Right Angle Triangle

1 1 1 1 1 1 1 
2 2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 
5 5 5 
6 6 
7 


'''

n = int(input())
num = 1
for row in range(n):
    for col in range(row,n):
        print(num,end=" ")
    num = num + 1
    print()
    
    
    
    
    
    
    


'''
Number Pattern - 10 : 1,22,333 in order for Right Aligned Right Angle Triangle

              1 
            2 2 
          3 3 3 
        4 4 4 4 
      5 5 5 5 5 
    6 6 6 6 6 6 
  7 7 7 7 7 7 7 



'''

n = int(input())  # 7
num = 1
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row+1):
        print(num,end=" ")
    num = num + 1
    print()
    
    
    
    
    
    
    
    
    
'''
Number Pattern - 11 : 1,22,333 in order for Right Aligned Inverted Right Angle Triangle

  1 1 1 1 1 1 1 
    2 2 2 2 2 2 
      3 3 3 3 3 
        4 4 4 4 
          5 5 5 
            6 6 
              7 

'''

n = int(input()) # 7
num = 1
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n):
        print(num,end=" ")
    num = num + 1
    print()
    
    
    
    
    
    
    
    
    
    
    



'''
Number Pattern - 12 : 1,222,33333 in order, for Hill Pattern 

              1 
            2 2 2 
          3 3 3 3 3 
        4 4 4 4 4 4 4 
      5 5 5 5 5 5 5 5 5 
    6 6 6 6 6 6 6 6 6 6 6 
  7 7 7 7 7 7 7 7 7 7 7 7 7 



'''

n = int(input())
num = 1
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print(num,end=" ")
    for col in range(row+1):
        print(num,end=" ")
    num = num + 1
    print()
    
    
    
    
    
    
    



'''
Number Pattern - 13 : 1,222,33333 in order, for Reverse Hill Pattern 

  1 1 1 1 1 1 1 1 1 1 1 1 1 
    2 2 2 2 2 2 2 2 2 2 2 
      3 3 3 3 3 3 3 3 3 
        4 4 4 4 4 4 4 
          5 5 5 5 5 
            6 6 6 
              7 

'''

n = int(input())
num = 1
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print(num,end=" ")
    for col in range(row,n):
        print(num,end=" ")
    num = num + 1
    print()
    
    
    
    
    
    
    
    
    
    
    
    





'''
Number Pattern  - 14 : 5, 44,333,2222,11111 in order, for Left Aligned Right Angle Triangle 


5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1


'''

n = int(input())
num = n
for row in range(n):
    for col in range(row+1):
        print(num,end=" ")
    num = num -1
    print()
    
    
    
    
    
    
    
'''
Number Pattern - 15 : 55555,4444,333,22,1 in order, for Inverted Left Aligned Right Angle Triangle 


5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 


'''

n = int(input())
num = n
for row in range(n):
    for col in range(row,n):
        print(num,end=" ")
    num = num - 1
    print()
    
    
    
    
    
    
    
    
    
    
    
'''
Number Pattern - 16 : 5,44,333,2222,11111 in order, for Right Aligned Right Angle Triangle 

          5 
        4 4 
      3 3 3 
    2 2 2 2 
  1 1 1 1 1


'''

n = int(input())
num = n
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row+1):
        print(num,end=" ")
    num = num - 1
    print()




