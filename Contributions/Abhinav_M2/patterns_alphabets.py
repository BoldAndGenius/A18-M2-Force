# Abhinav Anand
# Alphabet Pattern
print("Welcome to Alphabet Pattern programming\n")

try:
    # (example)
    # size = 5              word = A    |   word = Hello
    
    # [ - - - - -             * * *     |   *       *   * * * * *   *           *             * * *
    #   - - - - -           *       *   |   *       *   *           *           *           *       *
    #   - - - - -           * * * * *   |   * * * * *   * * *       *           *           *       *
    #   - - - - -           *       *   |   *       *   *           *           *           *       *
    #   - - - - -  ] 5x5    *       *   |   *       *   * * * * *   * * * * *   * * * * *     * * *

    size = int(input("Enter a number for matrix size (greater than 4): ").strip())

    word_list = []
    # if Matrix_size is number (integer) then below program runs or else throws error
    if size>4:
        # -------------------------------------------------
        # Pattern for Alphabets
        def char_pattern(matrix_size):
            for row in range(matrix_size):
                row_pattern = ""
                for col in range(matrix_size):
                    if char(row,col,matrix_size):
                        # print("*",end=" ")
                        row_pattern+="*"
                    else:
                        # print(" ",end=" ")
                        row_pattern+=" "
                    row_pattern+=" "
                # print()
                word_list.append(row_pattern)
            # print()
        # -------------------------------------------------
        word = input("Enter a letter or word for pattern : ")
        # word = "ABCDefghijklMnopQRstuvwxYz"
        print()

        for option in word.upper():
            # condition for alphabets

            match(option):
                case "A":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not (col==0 or col==matrix_size-1)) or (col==0 and not row==0) or row==matrix_size//2 or (col==matrix_size-1 and not row==0) # A
                case "B":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or col==0 or (row==matrix_size//2 and not col==matrix_size-1) or (col==matrix_size-1 and not (row==0 or row==matrix_size-1 or row==matrix_size//2)) or (row==matrix_size-1 and not col==matrix_size-1) # B
                case "C":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==0) or (col==0 and not (row==0 or row==matrix_size-1)) or (row==matrix_size-1 and not col==0) # C
                case "D":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or col==0 or (col==matrix_size-1 and not (row==0 or row==matrix_size-1)) or (row==matrix_size-1 and not col==matrix_size-1) # B
                case "E":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==0 or (row==matrix_size//2 and col<matrix_size//2+1) or row==matrix_size-1  # E
                case "F":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==0 or (row==matrix_size//2 and col<matrix_size//2+1)  # F
                case "G":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or row==0 or row==matrix_size-1 or (row==matrix_size//2 and col>=matrix_size//2) or (col==matrix_size-1 and row>matrix_size//2) # G
                case "H":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or row==matrix_size//2 or col==matrix_size-1 # H
                case "I":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or row==matrix_size-1 or col==matrix_size//2 # I
                case "J":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==matrix_size//2 or (col==0 and row>matrix_size//2) or (row==matrix_size-1 and col<matrix_size//2) # J
                case "K":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or (row-(matrix_size//2)*2==col-matrix_size//2 ) or ((row + col)*2==matrix_size-1) # K
                case "L":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or row==matrix_size-1 # L
                case "M":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or col==matrix_size-1 or (row==col and row<matrix_size//2+1) or (row + col==matrix_size-1 and row<matrix_size//2) # M
                case "N":
                    def char(row=0,col=0,matrix_size=size):
                        return row==col or col==0 or col==matrix_size-1 # N
                case "O":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not (col==0 or col==matrix_size-1)) or (col==0 and not (row==0 or row==matrix_size-1)) or (col==matrix_size-1 and not (row==0 or row==matrix_size-1)) or (row==matrix_size-1 and not (col==0 or col==matrix_size-1)) # O
                case "P":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or (row==matrix_size//2 and not col==matrix_size-1) or col==0 or (col==matrix_size-1 and row<matrix_size//2 and not row==0) # P
                case "Q":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==1 and not (col==0 or col==1 or col==matrix_size-1 or col==matrix_size-2)) or (col==1 and not (row==0 or row==1 or row==matrix_size-1 or row==matrix_size-2)) or (col==matrix_size-2 and not (row==0 or row==1 or row==matrix_size-1 or row==matrix_size-2)) or (row==matrix_size-2 and not (col==0 or col==1 or col==matrix_size-1 or col==matrix_size-2))  or (row==col and row>matrix_size//2)# Q
                case "R":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==matrix_size-1) or (row==matrix_size//2 and not col==matrix_size-1) or col==0 or (col==matrix_size-1 and row<matrix_size//2 and not row==0) or (row-(matrix_size//2)*2+1==col-matrix_size//2 ) # R
                case "S":
                    def char(row=0,col=0,matrix_size=size):
                        return (row==0 and not col==0) or (row==matrix_size//2 and not (col==0 or col==matrix_size-1)) or (row==matrix_size-1 and not col==matrix_size-1) or (col==0 and row<matrix_size//2 and not row==0) or (col==matrix_size-1 and row>matrix_size//2 and not row==matrix_size-1) # S
                case "T":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or col==matrix_size//2 # T
                case "U":
                    def char(row=0,col=0,matrix_size=size):
                        return (col==0 and not row==matrix_size-1) or (col==matrix_size-1 and not row==matrix_size-1) or (row==matrix_size-1 and not (col==0 or col==matrix_size-1)) # U
                case "V":
                    def char(row=0,col=0,matrix_size=size):
                        return ((col==0 or col==matrix_size-1) and row<matrix_size//2) or (row-(matrix_size//2)*2==col-matrix_size//2 ) or ((row + col)-matrix_size//2==matrix_size-1)  # V
                case "W":
                    def char(row=0,col=0,matrix_size=size):
                        return col==0 or col==matrix_size-1 or (row==col and row>matrix_size//2-1) or ((row+col)==matrix_size-1 and row>matrix_size//2)  # W
                case "X":
                    def char(row=0,col=0,matrix_size=size):
                        return row==col or row + col==matrix_size-1 # X
                case "Y":
                    def char(row=0,col=0,matrix_size=size):
                        return (col==matrix_size//2 and row>matrix_size//2) or (row==col and row<matrix_size//2+1) or (row + col==matrix_size-1 and row<matrix_size//2) # M
                case "Z":
                    def char(row=0,col=0,matrix_size=size):
                        return row==0 or row+col==matrix_size-1 or row==matrix_size-1 # Z
                case _:
                    def char(row=0,col=0,matrix_size=size):
                        return None
        
            char_pattern(matrix_size=size)
    else:
        print("For better Pattern visulaization try size greater than 4")
except Exception as error:
    # This statement block will execute when above block throws an error
    print(f"Error : {error}")


for iteration in range(size):
    print("  ".join([word_list[size*total_word+iteration] for total_word in range(len(word)) ]))
