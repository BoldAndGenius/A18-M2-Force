n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if col==row or col+row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()