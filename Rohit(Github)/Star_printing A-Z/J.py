n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or (row==n-1 and col<=n//2) or (row>n//2 and col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()