'''diagonal pattern'''
rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        if row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''L pattern'''
rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        if col==0 or row==(rows-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''Hollow Box pattern
where only the boundary (edges) of the box is filled with asterisks (*), while the inside remains hollow.
'''
rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        if row==0 or col==0 or row==(rows-1) or col==(columns-1) or row==(rows-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



'''Right Angle Triangle pattern'''
rows=int(input('Enter number of rows:'))
for row in range(rows):
    for value in range(row+1):
        print("*",end=" ")
    print()


'''Inverted Right Angle Triangle pattern'''
rows=int(input('Enter number of rows:'))
for row in range(rows,0,-1):
    for value in range(row):
        print("*",end=" ")
    print()

'''Pyramid pattern'''
rows=int(input('Enter number of rows:'))
for row in range(rows):
    for space in range(rows-row):
        print(" ",end="")
    for value in range(row+1):
        print("*",end=" ")
    print()

'''Diamond pattern'''
rows=int(input('Enter number of rows:'))
for row in range(rows):
    for space in range(rows-row):
        print(" ",end="")
    for value in range(row+1):
        print("*",end=" ")
    print()
for row in range(rows):
    for space in range(row+1):
        print(" ",end="")
    for value in range(rows-row,0,-1):
        print("*",end=" ")
    print()
