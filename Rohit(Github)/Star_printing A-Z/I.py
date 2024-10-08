n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()