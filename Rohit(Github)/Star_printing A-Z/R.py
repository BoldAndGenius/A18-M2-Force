n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if col==0 or (row==0 and col!=n-1) or (row==n//2 and col!=n-1) or (col==n-1 and 0<row<n//2) or (col==row-1 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()