# Abhinav Anand
# Alphabet Pattern
print("Welcome to Alphabet Pattern programming\n")

try:
    # size = 4 (example)
    # [ - - - -
    #   - - - -
    #   - - - -
    #   - - - -  ] 4x4
    size = int(input("Enter a number for matrix size (greater than 4): ").strip())

    # if Matrix_size is number (integer) then below program runs or else throws error
    if size>4:
        # -------------------------------------------------
        # Pattern for Alphabets
        def char_pattern(matrix_size):
            for row in range(matrix_size):
                for col in range(matrix_size):
                    if char(row,col,matrix_size):
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
                print()
            print()
        # -------------------------------------------------
        word_list = []
        word = input("Enter a letter or word for pattern : ")
        # word = "ABCDefghijklMnopQRstuvwxYz"
        print()

        for option in word.upper():
            # condition for alphabets

            match(option):
                case "A":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not (col==0 or col==matrix_size-1)) or (col==0 and not row==0) or row==matrix_size//2 or (col==matrix_size-1 and not row==0) # A
                    char_pattern(matrix_size=size)
                case "B":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or col==0 or (row==matrix_size//2 and not col==matrix_size-1) or (col==matrix_size-1 and not (row==0 or row==matrix_size-1 or row==matrix_size//2)) or (row==matrix_size-1 and not col==matrix_size-1) # B
                    char_pattern(matrix_size=size)
                case "C":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==0) or (col==0 and not (row==0 or row==matrix_size-1)) or (row==matrix_size-1 and not col==0) # C
                    char_pattern(matrix_size=size)
                case "D":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or col==0 or (col==matrix_size-1 and not (row==0 or row==matrix_size-1)) or (row==matrix_size-1 and not col==matrix_size-1) # B
                    char_pattern(matrix_size=size)
                case "E":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==0 or (row==matrix_size//2 and col<matrix_size//2+1) or row==matrix_size-1  # E
                    char_pattern(matrix_size=size)
                case "F":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==0 or (row==matrix_size//2 and col<matrix_size//2+1)  # F
                    char_pattern(matrix_size=size)
                case "G":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or row==0 or row==matrix_size-1 or (row==matrix_size//2 and col>=matrix_size//2) or (col==matrix_size-1 and row>matrix_size//2) # G
                    char_pattern(matrix_size=size)
                case "H":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or row==matrix_size//2 or col==matrix_size-1 # H
                    char_pattern(matrix_size=size)
                case "I":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or row==matrix_size-1 or col==matrix_size//2 # I
                    char_pattern(matrix_size=size)
                case "J":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==matrix_size//2 or (col==0 and row>matrix_size//2) or (row==matrix_size-1 and col<matrix_size//2) # J
                    char_pattern(matrix_size=size)
                case "K":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or (row-(matrix_size//2)*2==col-matrix_size//2 ) or ((row + col)*2==matrix_size-1) # K
                    char_pattern(matrix_size=size)
                case "L":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or row==matrix_size-1 # L
                    char_pattern(matrix_size=size)
                case "M":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or col==matrix_size-1 or (row==col and row<matrix_size//2+1) or (row + col==matrix_size-1 and row<matrix_size//2) # M
                    char_pattern(matrix_size=size)
                case "N":
                    def char(row=0,col=0,matrix_size=size):
                        return row==col or col==0 or col==matrix_size-1 # N
                    char_pattern(matrix_size=size)
                case "O":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not (col==0 or col==matrix_size-1)) or (col==0 and not (row==0 or row==matrix_size-1)) or (col==matrix_size-1 and not (row==0 or row==matrix_size-1)) or (row==matrix_size-1 and not (col==0 or col==matrix_size-1)) # O
                    char_pattern(matrix_size=size)
                case "P":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or (row==matrix_size//2 and not col==matrix_size-1) or col==0 or (col==matrix_size-1 and row<matrix_size//2 and not row==0) # P
                    char_pattern(matrix_size=size)
                case "Q":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==1 and not (col==0 or col==1 or col==matrix_size-1 or col==matrix_size-2)) or (col==1 and not (row==0 or row==1 or row==matrix_size-1 or row==matrix_size-2)) or (col==matrix_size-2 and not (row==0 or row==1 or row==matrix_size-1 or row==matrix_size-2)) or (row==matrix_size-2 and not (col==0 or col==1 or col==matrix_size-1 or col==matrix_size-2))  or (row==col and row>matrix_size//2)# Q
                    char_pattern(matrix_size=size)
                case "R":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or (row==matrix_size//2 and not col==matrix_size-1) or col==0 or (col==matrix_size-1 and row<matrix_size//2 and not row==0) or (row-(matrix_size//2)*2+1==col-matrix_size//2 ) # R
                    char_pattern(matrix_size=size)
                case "S":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==0) or (row==matrix_size//2 and not (col==0 or col==matrix_size-1)) or (row==matrix_size-1 and not col==matrix_size-1) or (col==0 and row<matrix_size//2 and not row==0) or (col==matrix_size-1 and row>matrix_size//2 and not row==matrix_size-1) # S
                    char_pattern(matrix_size=size)
                case "T":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==matrix_size//2 # T
                    char_pattern(matrix_size=size)
                case "U":
                    def char(row=0,col=0,matrix_size=size):
                        return (col==0 and not row==matrix_size-1) or (col==matrix_size-1 and not row==matrix_size-1) or (row==matrix_size-1 and not (col==0 or col==matrix_size-1)) # U
                    char_pattern(matrix_size=size)
                case "V":
                    def char(row=0,col=0,matrix_size=size):
                        return ((col==0 or col==matrix_size-1) and row<matrix_size//2) or (row-(matrix_size//2)*2==col-matrix_size//2 ) or ((row + col)-matrix_size//2==matrix_size-1)  # V
                    char_pattern(matrix_size=size)
                case "W":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or col==matrix_size-1 or (row==col and row>matrix_size//2-1) or ((row+col)==matrix_size-1 and row>matrix_size//2)  # W
                    char_pattern(matrix_size=size)
                case "X":
                    def char(row=0,col=0,matrix_size=size):
                        return row==col or row + col==matrix_size-1 # X
                    char_pattern(matrix_size=size)
                case "Y":
                    def char(row=0,col=0,matrix_size=size):
                        return (col==matrix_size//2 and row>matrix_size//2) or (row==col and row<matrix_size//2+1) or (row + col==matrix_size-1 and row<matrix_size//2) # M
                    char_pattern(matrix_size=size)
                case "Z":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or row+col==matrix_size-1 or row==matrix_size-1 # Z
                    char_pattern(matrix_size=size)
                case _:
                    pass
        
    else:
        print("For better Pattern visulaization try size greater than 4")
except Exception as error:
    # This statement block will execute when above block throws an error
    print(f"Error : {error}")
