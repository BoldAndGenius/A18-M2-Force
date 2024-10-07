'''base programs of Patterns'''
n = int(input("Enter Number: ))
for row in range(n):
    for col in range(n):
        print((row,col),end=' ')            ## To give Matrix form
    print()
    
for row in range(5):
    for col in range(5):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''C Pattern'''
 
n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0:
            print('C',end = ' ')
        else:
            print(' ',end=' ')
    print()


'''E Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n-1 or row == n//2:
            print('E',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
'''F Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n//2:
            print('F',end = ' ')
        else:
            print(' ',end=' ')
    print()   

'''G Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n-1 or (row == n//2 and col>=n//2) or (col == n-1 and row >= n//2):
            print('G',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
'''H Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or row==n//2 :
            print('H',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''I Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == n//2:
            print('I',end = ' ')
        else:
            print(' ',end=' ')
    print()

''' J Pattern '''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or col == n//2  or (col==0 and row>=n//2) or (row==n-1 and col <= n//2):
            print('J',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
'''L Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == n-1:
            print('L',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''M Pattern''' 

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row==col and row<=n//2) or (row+col==(n-1) and row<=n//2):
            print('M',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''N Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == col or col == n-1:
            print('N',end = ' ')
        else:
            print(' ',end=' ')
    print()


'''O Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n-1 or col == n-1:
            print('O',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''P Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n//2 or (col==n-1 and row <= n//2):
            print('P',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''R Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n//2 or (col==n-1 and row <= n//2) or (row==col and row >= n//2):
            print('R',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''S Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or row == n//2 or (col==0 and row<=n//2) or (col==n-1 and row >= n//2) :
            print('S',end = ' ')
        else:
            print(' ',end=' ')
    print()
    
'''T Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == 0 or col == n//2 :
            print('T',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''U Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or row == n-1 :
            print('U',end = ' ')
        else:
            print(' ',end=' ')
    print()



'''W Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row==col and row>=n//2) or (row+col==(n-1) and row>=n//2):
            print('W',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''X Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row == col or row+col == n-1:
            print('X',end = ' ')
        else:
            print(' ',end=' ')
    print()

'''Y Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if (row == col and row <= n//2) or (row+col == n-1 and row <= n//2) or (col == n//2 and row >= n//2) :
            print('Y',end = ' ')
        else:
            print(' ',end=' ')
    print()


'''Z Pattern'''

n=int(input("Enter Number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row== n-1 or (row+col==n-1):
            print('Z',end = ' ')
        else:
            print(' ',end=' ')
    print()
    

    

    

