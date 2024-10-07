#-------------------- letter Z --------------------

n26 = int(input("enter a odd number for letter Z : "))

for row in range(n26):
    for col in range(n26):
        if row == 0 or row == n26-1 or row + col == n26:
            print("*", end = "")
        else:
            print(" ", end="")
    print()

# -------------------- letter Y ------------------------

n25 = int(input("enter a odd number for letter Y : "))

for row in range(n25):
    for col in range (n25):
        if (row == col and row <= n25//2) or row + col == n25 - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter X ------------------------

n24 = int(input("enter a odd number for letter Y : "))

for row in range(n24):
    for col in range(n24):
        if row + col == n24 - 1 or row == col:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter W ------------------------

n23 = int(input("enter a odd number for letter W : "))

for row in range(n23):
    for col in range(n23):
        if col == 0 or col == n23 - 1 or (row == col and row >= n23 // 2) or (row + col == n23 - 1 and row >= n23 // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter V ------------------------

n22 = int(input("enter a odd number for letter V : "))

for row in range(n22):
    for col in range(n22 * 2 - 1):
        if row == col or row + col == n22 * 2 - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter U ------------------------

n21 = int(input("enter a odd number for letter U : "))

for row in range(n21):
    for col in range(n21):
        if ((col == 0 or col == n21 - 1) and (row != n21 - 1)):
            print("*", end="")
        elif  (0 < col < n21 // 2 + 1) and (row == n21 - 1):
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter T ------------------------

n20 = int(input("enter a odd number for letter T : "))

for row in range(n20):
    for col in range(n20):
        if row == 0:
            print("* ", end="")
        elif col == n20 - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter S ------------------------

n19 = int(input("enter a odd number for letter S : "))

for row in range(n19):
    for col in range(n19 ):
        if (row == 0 or row == n19 - 1 or row == n19 // 2) and n19 // 2 > col > 0 :
            print("* ", end="")
        elif (col == 0 and 0 < row < n19 // 2) or (col == n19 - 2  and n19 - 1 > row > n19 // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter R ------------------------

n18 = int(input("enter a odd number for letter  R: "))

for row in range(n18):
    for col in range(n18):
        if (row == 0 or row == n18 // 2) and (1 < col < n18 // 2 + 1):
            print("* ", end="")
        elif (col == 0 or (col == n18 - 1 and row <= n18 // 2 - 1)) and (0 < row <= n18-1) or (row - col == n18 // 2 - 1 and row > n18 // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter Q ------------------------

n17 = int(input("enter a odd number for letter Q : "))

for row in range(n17):
    for col in range(n17):
        if (row == 0 or row == n17 - 2) and (0 < col < n17 // 2 + 1):
            print("* ", end="")
        elif ((col == 0 or col == n17 - 1) and (0 < row < n17 - 2)) or (row == col and row >= n17 // 2 and col != n17 - 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter P ------------------------

n16 = int(input("enter a odd number for letter P : "))

for row in range(n16):
    for col in range(n16):
        if (row == 0 or row == n16 // 2) and (1 < col < n16 // 2 + 1):
            print("* ", end="")
        elif (col == 0 or (col == n16 - 1 and row <= n16 // 2 - 1)) and (0 < row < n16-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter O ------------------------

n15 = int(input("enter a odd number for letter O : "))

for row in range(n15):
    for col in range(n15):
        if (row == 0 or row == n15 - 1) and (0 < col < n15 // 2 + 1):
            print("* ", end="")
        elif (col == 0 or col == n15 - 1) and (0 < row < n15-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter N ------------------------

n14 = int(input("enter a odd number for letter N : "))

for row in range(n14):
    for col in range(n14):
        if col == 0 or col == n14 - 1 or (row == col):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter M ------------------------

n13 = int(input("enter a odd number for letter M : "))

for row in range(n13):
    for col in range(n13):
        if col == 0 or col == n13 - 1 or (row == col and row <= n13 // 2) or (row + col == n13 - 1 and row <= n13 // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter L ------------------------

n12 = int(input("enter a odd number for letter L : "))

for row in range(n12):
    for col in range(n12):
        if col == 0:
            print("*", end="")
        elif row == n12 - 1:
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter K ------------------------

n11= int(input("enter a odd number for letter K : "))

for row in range(n11):
    for col in range(n11):
        if col == 0 or ((row + col == n11 // 2) and (col > 0)) or ((row - col == n11 // 2) and (col > 0)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter J ------------------------

n10= int(input("enter a odd number for letter J : "))

for row in range(n10):
    for col in range(n10):
        if (col == n10 // 2 and row < n10 - 1) or row == 0 or (col == 0 and n10 // 2 < row < n10 -1) or (row == n10 -1 and 0 < col < n10 // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter I ------------------------

n9= int(input("enter a odd number for letter I : "))

for row in range(n9):
    for col in range(n9):
        if col == n9 // 2 or row == 0 or row == n9 - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter H ------------------------

n8= int(input("enter a odd number for letter H : "))

for row in range(n8):
    for col in range(n8):
        if col == 0 or col == n8-1 or row == n8 // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter G ------------------------

n7 = int(input("Enter a odd number for letter G :"))
for row in range(n7):
    for col in range(n7):
        if (row==0 and col!=0)  or (col==0 and row!=n7-1 and row!=0) or (row==n7-1 and col!=n7-1 and col!=0) or (row==n7//2 and col>=n7//2) or (row>=n7//2 and col==n7-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# -------------------- letter F ------------------------

n6= int(input("enter a odd number for letter F : "))

for row in range(n6):
    for col in range(n6):
        if col == 0:
            print("*", end="")
        elif (row == 0 or row == n6 // 2) and col > 1:
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter E ------------------------

n5= int(input("enter a odd number for letter E : "))

for row in range(n5):
    for col in range(n5):
        if col == 0:
            print("*", end="")
        elif (row == 0 or row == n5 // 2 or row == n5 - 1) and col > 1:
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter D ------------------------

n4 = int(input("enter a odd number for letter D : "))

for row in range(n4):
    for col in range(n4 * 2 - 1):
        if col == 0 or (col == n4 * 2 - 2 and 0 < row < n4 - 1):
            print("*", end="")
        elif (row == 0 or row == n4 - 1) and (1 < col < n4):
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter C ------------------------

n3= int(input("enter a odd number for letter C : "))

for row in range(n3):
    for col in range(n3):
        if col == 0 and 0 < row < n3 - 1:
            print("*", end="")
        elif (row == 0 or row == n3 - 1) and col != 0:
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# -------------------- letter B ------------------------

n2 = int(input("enter a odd number for letter B : "))

for row in range(n2):
    for col in range(n2):
        if (col == 0 and 0 < row < n2 - 1) or (col == n2 - 1 and 0 < row < n2 - 1 and row != n2 // 2) or (row == 0 and col < n2 - 4) or (row == n2 - 1 and col < n2 - 4) or (row == n2 // 2 and col < n2 - 4):
            print("*", end=" ")
        else:
            print(" ", end="")
    print()

# ----------------------- letter A --------------------------

n1 = int(input("enter a odd number for letter A : "))

for row in range(n1):
    for col in range(2 * n1 - 1):
        if col == n1 - 1 - row or col == n1 -1 + row and col != n1 - 1 + (n1//2):
            print("*", end="")
        elif row == n1 // 2 and (col > n1 - row and col < n1 + 1):
            print("* ", end="")
        else:
            print(" ", end="")
    print()

    