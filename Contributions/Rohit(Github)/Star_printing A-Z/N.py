n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()