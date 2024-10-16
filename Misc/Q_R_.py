#  word:"Q"
n=5
for row in range(5):
    for col in range(5):
        if (col==0 and row <n-1) or (col==n-2 and row<n-1) or (row==0 and col<n-1) or (row==n-2 and col<n-1) or (row==col and row>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#  word:"R"
n=5
for row in range(5):
    for col in range(5):
        if row in(0,n//2) or col==0 or (col==n-1 and row<n//2) or (row==col and row>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()