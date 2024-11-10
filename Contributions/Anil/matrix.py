'''indices or positions of specific elements in the matrix'''
rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        print((row,col),end=" ")
    print()

'''Entering values and display of matrix'''
rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
matrix=[]
for row in range(rows):
    matrix.append([])
    for col in range(columns):
       value=int(input(f'Enter value for matrix[{row,col}]:'))
       matrix[row].append(value)
for index in range(len(matrix)):
    print(matrix[index])


