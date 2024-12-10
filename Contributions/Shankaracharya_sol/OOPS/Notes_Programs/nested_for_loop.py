'''
#WAP to print all the alphabets
collection = input("Enter a name:")
n = 11
for item in collection:
    if item in "Aa":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n - 1 or row == 0 or row == n // 2 :
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Bb":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n-1 or row == 0 or row == n//2 or row == n-1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Cc":
        for row in range(n):
            for col in range(n):
                if col == 0 or row == 0 or row == n - 1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "DdOo":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n-1 or row == 0 or row == n-1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Ee":
        for row in range(n):
            for col in range(n):
                if col == 0 or row == 0 or row == n//2 or row == n-1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Ff":
        for row in range(n):
            for col in range(n):
                if col == 0 or row == 0 or row == n//2:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Gg":
        for row in range(n):
            for col in range(n):
                if col == 0 or row == 0 or row == n-1 or (col == n-1 and row >= n//2) or (row == n//2 and col >= n//2):
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Hh":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n - 1 or row == n // 2 :
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Ii":
        for row in range(n):
            for col in range(n):
                if row == 0 or row == n - 1 or col == n // 2 :
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Jj":
        for row in range(n):
            for col in range(n):
                if row == 0 or col == n // 2 or (row == n - 1 and col <= n // 2) or (col == 0 and row >= n // 2) :
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Kk":
        for row in range(n):
            for col in range(n):
                if col == 0 or (row-col == n//2 and row>=n//2) or (row+col == n//2 and row <= n//2):
                
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Ll":
        for row in range(n):
            for col in range(n):
                if col == 0 or row == n - 1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Mm":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n - 1 or (row == col and row <= n // 2) or (row + col == n - 1 and row <= n //2):
                
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Nn":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n - 1 or row == col:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Pp":
        for row in range(n):
            for col in range(n):
                if col == 0 or row == 0 or row == n // 2 or (col == n - 1 and row <= n // 2):
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Qq":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n-1 or row == 0 or row == n-1 or (row == col and row >= n // 2):
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Rr":
        for row in range(n):
            for col in range(n):
                if col == 0 or (row == 0 and col <= n//2) or (row == n // 2 and col <= n//2) or (col == n//2 and row <= n//2) or ((row>=n//2 and col<=n//2) and (row-col == n//2)):
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()
    
    elif item in "Ss":
        for row in range(n):
            for col in range(n):
                if (row == 0) or (row == n // 2) or (row == n - 1) or (col == 0 and row <= n // 2) or (col== n-1 and row >= n//2):
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Tt":
        for row in range(n):
            for col in range(n):
                if row == 0 or col == n // 2:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()
    
    elif item in "Uu":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n - 1 or row == n - 1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()
    
    elif item in "Ww":
        for row in range(n):
            for col in range(n):
                if col == 0 or col == n - 1 or (row + col == n-1 and col <= n // 2) or (row == col and col >= n // 2) :
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()
        
    elif item in "Xx":
        for row in range(n):
            for col in range(n):
                if row + col == n-1 or row == col:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()

    elif item in "Yy":
        for row in range(n):
            for col in range(n):
                if (row == col and row <= n // 2) or (row + col == n - 1 and row <= n // 2) or (col == n//2 and row >= n // 2) :
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        print()
        
    elif item in "Zz":
        for row in range(n):
            for col in range(n):
                if row == 0 or row == n - 1 or row + col == n - 1:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
          
              '''
n=9
for row in range(n):
    for col in range(n):
        if row + col >= n and row <= n//2:
            print(" ",end = " ")
        else:
            
            print("*",end = " ")
    print()
print()
n=7
for row in range(n):
    for col in range(n):
        if (row > col and row+col <= n-2) or (col >  row and row + col >= n):
            print(" ",end = " ")
        else:
            
            print("*",end = " ")
    print()
print()


for row in range(n):
    for col in range(n):
        if row == n//2 or col == n//2 or row+col==n//2 or row-col==n//2 or col-row==n//2 or row+col == n+2:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
