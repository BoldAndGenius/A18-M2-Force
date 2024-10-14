for row in range(5):
    for col in range (5):
        if row ==0 or row==4 or col==0 or col==4 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
*       *
*       *
*       *
* * * * *
"""

for row in range(5):
    for col in range (5):
        if row ==0 or row==4 or col==0 or col==4 or row==col or row<=col or col<=row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""""
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
# """

# ALPHABETS FROM A TO Z...................


for row in range(5):
    for col in range (5):
        if row==0 or col==0 or col==4 or row==5//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

""""
* * * * * 
*       *
* * * * *
*       *
*       *

"""

for row in range(5):
    for col in range (5):
        if col==0 or row==0 or row ==4 or col==4 or row==5//2 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""""
* * * * * 
*       *
* * * * *
*       *
* * * * *

"""

for row in range(5):
    for col in range (5):
        if col==0 or row==0 or row ==4  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
*
*
*
* * * * *

"""

for row in range(5):
    for col in range (5):
        if row ==0 or row==4 or col==0 or col==4 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
*       *
*       *
*       *
* * * * *
"""  

for row in range(5):
    for col in range (5):
        if row ==0 or row==4 or col==0 or row==5//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
*
* * * * *
*
* * * * *
"""
for row in range(5):
    for col in range (5):
        if row ==0 or col==0 or row==5//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
*
* * * * *
*
*
"""

for row in range(5):
    for col in range (5):
        if row ==0 or col==0 or row==4 or (col==4 and row>=5//2) or (row==5//2 and col>=5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
*
*   * * *
*       *
* * * * *

"""

for row in range(5):
    for col in range (5):
        if  col==0 or col==4 or row==5//2 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
*       *
* * * * *
*       *
*       *

"""


for row in range(5):
    for col in range (5):
        if  col==5//2 or row==0 or row==4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
    *
    *
    *
* * * * *

"""

for row in range(5):
    for col in range (5):
        if  col==5//2 or row==0 or (row==4 and col<=5//2) or (col==0 and row>=5//2+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * * 
    *
    *
*   *
* * *

"""

for row in range(5):
    for col in range (5):
        if  col==5//2 or (row+col==4 and row<=5//2)or(row==col and col>=5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''''

    *   * 
    * *
    *
    * *
    *   *
'''''

for row in range(5):
    for col in range (5):
        if  col==5//2 or (row==4 and col>=5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
    *     
    *
    *
    *
    * * *
"""


for row in range(5):
    for col in range (5):
        if  col==0 or col==4 or (row==col and col<=5//2) or (row+col==4 and col>=5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
* *   * *
*   *   *
*       *
*       *
"""

for row in range(5):
    for col in range (5):
        if col==0 or row==col or col==4 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
* *     *
*   *   *
*     * *
*       *
"""

for row in range(5):
    for col in range (5):
        if col==1 or col==3 or (row==0 and col==5//2) or (row==4 and col==5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
  * * *   
  *   *
  *   *
  *   *
  * * *
"""

for row in range(5):
    for col in range (5):
        if col==5//2 or(row==0 and col>=5//2) or (col==4 and row<=5//2) or (row==5//2 and col>=5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
    * * * 
    *   *
    * * *
    *
    *

"""


for row in range(5):
    for col in range (5):
        if (row==0 and col==5//2) or (col==1 and row<=5//2+1) or (row==3 and col==5//2 ) or (col==3 and row<=5//2+1) or(row==col and col>=5//2) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
  * * *   
  *   *
  * * *
  * * *
        *
"""

for row in range(5):
    for col in range (5):
        if col==1 or col==3 or (row==4 and col==5//2) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
  *   *   
  *   *
  *   *
  *   *
  * * *

"""
for row in range(5):
    for col in range (5):
        if (col==row and col<=5//2) or (col+row==4 and row<=5//2) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
  *   *
    *
"""

for row in range(5):
    for col in range (5):
        if col==0 or col==4 or (row+col==4 and row>=5//2) or (row==col and col>=5//2) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
*       *
*   *   *
* *   * *
*       *
"""
for row in range(5):
    for col in range (5):
        if col+row==4 or row==col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
  *   *
    *
  *   *
*       *
"""

for row in range(5):
    for col in range (5):
        if col+row==4 or (row==col and col<=5//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       * 
  *   *
    *
  *
*
"""

for row in range(5):
    for col in range (5):
        if row==0 or row==4 or row+col==4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * *
      *
    *
  *
* * * * *

"""