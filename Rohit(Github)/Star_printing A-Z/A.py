n = int(input("Enter the size : "))
for row in range(n):
    for col in range(2 * n - 1):
        if col == n - 1 - row or col == n -1 + row and col != n - 1 + (n//2):
            print("*", end="")
        elif row == n // 2 and (col > n - row and col < n + 1):
            print("* ", end="")
        else:
            print(" ", end="")
    print()


