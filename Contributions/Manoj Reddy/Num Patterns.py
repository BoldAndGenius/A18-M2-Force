## 2 Pattern

num = int(input("Enter Number: "))
for row in range(num):
    for col in range(num):
        if row == 0 or row == num-1 or  row == num//2 or (col==num-1 and row <= num//2) or (col == 0 and row >= num//2):
            print('2',end=' ')
        else:
            print(' ',end=' ')
    print()
    
## 3 Pattern

num = int(input("Enter Number: "))
for row in range(num):
    for col in range(num):
        if row == 0 or row == num-1 or  row == num//2 or col==num-1 :
            print('3',end=' ')
        else:
            print(' ',end=' ')
    print()
    
## 5 Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or row == n//2 or (col==0 and row<=n//2) or (col==n-1 and row >= n//2) :
            print('5',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
## 6 Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or row == n//2 or col==0 or (col==n-1 and row >= n//2) :
            print('6',end = ' ')
        else:
            print(' ',end=' ')
    print()

## 7 Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row+col==n-1 :
            print('7',end = ' ')
        else:
            print(' ',end=' ')
    print()

## 8 Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0 or col == n-1 or row == n//2:
            print('8',end = ' ')
        else:
            print(' ',end=' ')
    print()

# 9 Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n//2 or col == n-1 or (col==0 and row<=n//2):
            print('9',end = ' ')
        else:
            print(' ',end=' ')
    print()

## 0 Pattern

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1 :
            print('0',end = ' ')
        else:
            print(' ',end=' ')
    print()