# #base programs of Patterns

for row in range(5):
    for col in range(5):
        print((row,col),end=' ')
    print()
    
for row in range(5):
    for col in range(5):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

## M Pattern 

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row==col and row<=n//2) or (row+col==(n-1) and row<=n//2):
            print('M',end = ' ')
        else:
            print(' ',end=' ')
    print()

## W Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row==col and row>=n//2) or (row+col==(n-1) and row>=n//2):
            print('W',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
## H Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or row==n//2 :
            print('H',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
## Z Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row== n-1 or (row+col==n-1):
            print('Z',end = ' ')
        else:
            print(' ',end=' ')
    print()