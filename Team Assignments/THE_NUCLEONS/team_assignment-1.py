n = int(input("enter a number : "))
for row in range(n):
    for col in range(n):
        if (row >= col and row <= n//2) or (row + col >= n-1 and col <= n//2) or (row <= col and row >= n//2) or (row + col <= n-1 and col >= n//2 ):
            print("*",end = " ")
        else:
            print(" ",end = " ")    
    print()        