# Print R 


n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (col==n-1  and row<=n//2) or row==n//2 or (row==col and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()