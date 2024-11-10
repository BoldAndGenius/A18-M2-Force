
n=int(input('Enter no of rows:'))


'''C'''

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print()  #to get next pattern on by giving one line gap

'''E'''
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n//2 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


'''F'''
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or  row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap

'''G'''
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (row==n//2 and col>=n//2) or row==n-1 or (col==n-1 and row>=n//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()    #to get next pattern on by giving one line gap

'''H'''
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()    #to get next pattern on by giving one line gap

'''I'''
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap


'''J'''
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or (row==n-1 and col<=n//2) or (col==0 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap

'''L'''
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print()   #to get next pattern on by giving one line gap




'''M'''
for row in range(n):
    for col in range(n):
        if col==0 or (row==col and row<=n//2)  or (row+col==n-1 and row<=n//2) or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap


'''N'''

for row in range(n):
    for col in range(n):
        if col==0 or row==col or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap

'''P'''
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or (col==n-1 and row<=n//2) or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()   #to get next pattern on by giving one line gap


'''R'''
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or (col==n-1 and row<=n//2) or row==n//2  or (row==col and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap


'''S'''
for row in range(n):
    for col in range(n):
        if row==0 or (col==0 and row<=n//2) or row==n//2 or (col==n-1 and row>=n//2) or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap

'''T'''

for row in range(n):
    for col in range(n):
        if row==0 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print() #to get next pattern on by giving one line gap

'''U'''
for row in range(n):
    for col in range(n):
        if col==0 or  row==n-1 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap

'''W'''
for row in range(n):
    for col in range(n):
        if col==0 or (row+col==n-1 and row>=n//2)  or (row==col and row>=n//2) or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print()   #to get next pattern on by giving one line gap


'''X'''
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()   #to get next pattern on by giving one line gap


'''Y'''
for row in range(n):
    for col in range(n):
        if (row==col and row<=n//2) or (row+col==n-1 and row<=n//2) or (col==n//2 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print()   #to get next pattern on by giving one line gap

'''Z'''
for row in range(n):
    for col in range(n):
        if row==0 or row+col==n-1 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

