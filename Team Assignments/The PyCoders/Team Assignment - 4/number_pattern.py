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







'''
Number Pattern - 17 : 55555,4444,333,22,1 in order, for Right Aligned Inverted Right Angle Triangle 


  5 5 5 5 5 
    4 4 4 4 
      3 3 3 
        2 2 
          1 
          
'''

n = int(input())
num = n
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n):
        print(num,end=" ")
    num = num - 1
    print()





'''
Number Pattern - 18: 5,444,33333,2222222,111111111 in order, for Hill Pattern. 

          5 
        4 4 4 
      3 3 3 3 3 
    2 2 2 2 2 2 2 
  1 1 1 1 1 1 1 1 1 


'''

n = int(input())
num = n
for row in range(n):
    for col in range(row,n):
        print(" ",end=" ")
    for col in range(row):
        print(num,end=" ")
    for col in range(row+1):
        print(num,end=" ")
    num = num - 1
    print()




'''
Number Pattern - 19: 5,444,33333,2222222,111111111 in order, for Reverse Hill Pattern 

 5 5 5 5 5 5 5 5 5 
    4 4 4 4 4 4 4 
      3 3 3 3 3 
        2 2 2 
          1 

'''


n = int(input())
num = n
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for col in range(row,n-1):
        print(num,end=" ")
    for col in range(row,n):
        print(num,end=" ")
    num = num - 1
    print()
    
    
    
    
    
    
    


'''
Number Pattern - 20 : 0,22,444,6666,88888 in order, for Left Aligned Right Angle Triangle.


0 
2 2 
4 4 4 
6 6 6 6 
8 8 8 8 8 

'''

n = int(input())  # 5
num = 0
for row in range(n):
    for col in range(row+1):
        print(num,end=" ")
    num = num + 2
    print()
    
    
    
  
  
  
'''
Number Pattern - 21

1 
2 2 
1 1 1 
2 2 2 2 
1 1 1 1 1

'''

n = int(input())
for row in range(n):
  for col in range(row+1):
    if row%2 == 0:
      print("1",end=" ")
    else:
      print("2",end=" ")
  print()
    
    
    
    
    
  
'''
Number Pattern - 22

  # # # # # 
    $ $ $ $ 
      # # # 
        $ $ 
          # 
          
'''

n = int(input())
for row in range(n):
  for col in range(row+1):
    print(" ",end=" ")
  for col in range(row,n):
    if row%2==0:
      print("#",end=" ")
    else:
      print("$",end=" ")
  print()
  
  




'''
Number Pattern - 23

          a 
        b b b 
      a a a a a 
    b b b b b b b 
  a a a a a a a a a 

'''

n = int(input())  # 5
for row in range(n):
  for col in range(row,n):
    print(" ",end=" ")
  for col in range(row):
    if row%2 == 0:
      print("a",end=" ")
    else:
      print("b",end=" ")
  for col in range(row+1):
    if row%2 == 0:
      print("a",end=" ")
    else:
      print("b",end=" ")
  print()
  
  
  
  
  
  


'''
Number Pattern - 24

A 
B B 
A A A 
B B B B 
A A A A A 

'''

n = int(input())  # 5
for row in range(n):
  for col in range(row+1):
    if row%2 == 0:
      print("A",end=" ")
    else:
      print("B",end=" ")
  print()
  
  
  




'''
Number Pattern - 25

  1 1 1 1 1 
    3 3 3 3 
      1 1 1 
        3 3 
          1


'''
n = int(input())
for row in range(n):
  for col in range(row+1):
    print(" ",end=" ")
  for col in range(row,n):
    if row%2 == 0:
      print("1",end=" ")
    else:
      print("3",end=" ")
  print()
  
  
  
  
  
  
  
  
  
  
  

'''
Number Pattern - 26

         # 
        $ $ $ 
      # # # # # 
    $ $ $ $ $ $ $ 
  # # # # # # # # # 

'''

n = int(input())
for row in range(n):
  for col in range(row,n):
    print(" ",end=" ")
  for col in range(row):
    if row%2==0:
      print("#",end=" ")
    else:
      print("$",end=" ")
  for col in range(row+1):
    if row%2 == 0:
      print("#",end=" ")
    else:
      print("$",end=" ")
  print()
  
  
  
  


'''
Number Pattern - 27

  1 1 1 1 1 1 1 1 1 
    0 0 0 0 0 0 0 
      1 1 1 1 1 
        0 0 0 
          1 


'''
n = int(input())  # 5
for row in range(n):
  for col in range(row+1):
    print(" ",end=" ")
  for col in range(row,n-1):
    if row%2 == 0:
      print("1",end=" ")
    else:
      print("0",end=" ")
  for col in range(row,n):
    if row%2 == 0:
      print("1",end=" ")
    else:
      print("0",end=" ")
  print()
    
    
    
    
    
    
    
'''
Number Pattern - 28 

          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 
    6 6 6 6 6 6 6 
      7 7 7 7 7 
        8 8 8 
          9 

'''

n = int(input())
num = 1
for row in range(n-1):
  for col in range(row,n):
    print(" ",end=" ")
  for col in range(row):
    print(num,end=" ")
  for col in range(row+1):
    print(num,end=" ")
  num = num + 1
  print()
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
Number Pattern - 29 

1                 1 
2 2             2 2 
3 3 3         3 3 3 
4 4 4 4     4 4 4 4 
5 5 5 5 5 5 5 5 5 5 
6 6 6 6     6 6 6 6 
7 7 7         7 7 7 
8 8             8 8 
9                 9 

'''

n = int(input())
num = 1
for row in range(n-1):
  for col in range(row+1):
    print(num,end=" ")
  for col in range(row,n-1):
    print(" ",end=" ")
  for col in range(row,n-1):
    print(" ",end=" ")  
  for col in range(row+1):
    print(num,end=" ")
  num = num + 1
  print()
for row in range(n):
  for col in range(row,n):
    print(num,end=" ")
  for col in range(row):
    print(" ",end=" ")
  for col in range(row):
    print(" ",end=" ")
  for col in range(row,n):
    print(num,end=" ")
  num = num + 1
  print()
  
  
  
  
  


'''
Number Pattern - 30 

1                 1 
2 2             2 2 
3 3 3         3 3 3 
4 4 4 4     4 4 4 4 
1 1 1 1 1 1 1 1 1 1 
2 2 2 2     2 2 2 2 
3 3 3         3 3 3 
4 4             4 4 
5                 5 



'''

n = int(input())
num = 1
for row in range(n-1):
  for col in range(row+1):
    print(num,end=" ")
  for col in range(row,n-1):
    print(" ",end=" ")
  for col in range(row,n-1):
    print(" ",end=" ")  
  for col in range(row+1):
    print(num,end=" ")
  num = num + 1
  print()
num = 1
for row in range(n):
  for col in range(row,n):
    print(num,end=" ")
  for col in range(row):
    print(" ",end=" ")
  for col in range(row):
    print(" ",end=" ")
  for col in range(row,n):
    print(num,end=" ")
  num = num + 1
  print()
  
  
  
  
  
  
  
'''
  
Number Pattern - 31 


          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  1 1 1 1 1 1 1 1 1 
    2 2 2 2 2 2 2 
      3 3 3 3 3 
        4 4 4 
          5 

'''

n = int(input())
num = 1
for row in range(n-1):
  for col in range(row,n):
    print(" ",end=" ")
  for col in range(row):
    print(num,end=" ")
  for col in range(row+1):
    print(num,end=" ")
  num = num + 1
  print()
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
    
Number Pattern - 32

          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 
    4 4 4 4 4 4 4 
      3 3 3 3 3 
        2 2 2 
          1 




'''

n = int(input())
num = 1
for row in range(n-1):
  for col in range(row,n):
    print(" ",end=" ")
  for col in range(row):
    print(num,end=" ")
  for col in range(row+1):
    print(num,end=" ")
  num = num + 1
  print()
# num = 1
for row in range(n):
  for col in range(row+1):
    print(" ",end=" ")
  for col in range(row,n-1):
    print(num,end=" ")
  for col in range(row,n):
    print(num,end=" ")
  num = num - 1
  print()
    
    
    
    
    
    
    
'''
Number Pattern - 33

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''
n = int(input())
for row in range(n):
  num = 1
  for col in range(row+1):
    print(num,end=" ")
    num = num + 1
  print()
  
  
  

'''
Number Pattern - 34

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

'''
n = int(input())
for row in range(n):
  num = 1
  for col in range(row,n):
    print(num,end=" ")
    num = num + 1
  print()
  
  
  
  
  
'''
Number Pattern - 35 

  1 2 3 4 5 
    1 2 3 4 
      1 2 3 
        1 2 
          1 

'''
n = int(input())
num = 1
for row in range(n):
  for col in range(row+1):
    print(" ",end=" ")
  num = 1
  for col in range(row,n):
    print(num,end=" ")
    num = num + 1
  print()
  


'''
Number Pattern - 36

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 

'''
n = int(input())
num = 1
for row in range(n):
  for col in range(row,n):
    print(" ",end=" ")
  num = 1
  for col in range(row+1):
    print(num,end=" ")
    num = num + 1
  print()