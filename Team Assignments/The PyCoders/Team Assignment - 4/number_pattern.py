'''
Number Pattern - 1

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