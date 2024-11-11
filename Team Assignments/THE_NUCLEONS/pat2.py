for col in range (5):
    for row in range(5):
        if row==0 or col==0 or row+col==4 or row + col<=4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""""
  * * * * * 
  * * * *
  * * *
  * *
  *
"""