
'''

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''

n = 5  # 5*5 Cross Matrix

for row in range(1,n+1):
    for col in range(row):
        print(col+1, end=" ")
    print()
    
    
   
   
   
   
    
'''

1
2 3
4 5 6
7 8 9 10


'''

n = 5
start = 1
for row in range(n):
    for col in range(row):
        print(start, end=" ")
        start = start + 1
    print()
        
  
  
  
  
  
  
  
  
        
    
'''

1 
3 5 
7 9 11 
13 15 17 19 
21 23 25 27 29 

'''    
    
n = 5
num = 1
for row in range(1, n+1):
    for col in range(row):
        print(num, end=" ")
        num = num + 2
    print()
    
    





'''
9 
8 7 
6 5 4 
3 2 1 9 
8 7 6 5 4 

'''
n = 5
num = 9
for row in range(1,n+1):
    for col in range(row):
        if num<1:
            num = 9
        print(num, end=" ")
        num = num - 1
    print()
    
    
    
    
'''
    1 
  2 3 
4 5 6 

'''
n = 3
num = 1
for row in range(1,n+1):
    print("  "*(n-row), end="")
    for col in range(row):
        print(num, end=" ")
        num = num + 1
    print()
        