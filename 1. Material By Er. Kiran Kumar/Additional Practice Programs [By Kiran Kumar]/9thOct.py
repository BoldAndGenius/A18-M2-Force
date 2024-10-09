
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
        
        