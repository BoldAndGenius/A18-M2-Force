n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if col==0 or (row==0 and col<n-1) or (row==n-1 and col<n-1) or (row==n//2 and col<n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()