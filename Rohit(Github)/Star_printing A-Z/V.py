n = int(input("Enter the size : "))
for row in range(n):
    for col in range(n * 2 - 1):
        if row == col or row + col == n * 2 - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()