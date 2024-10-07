n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if (col==0 and row!=n-1) or (col==n-1 and row!=n-1) or (row==n-1 and 0<col<n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()