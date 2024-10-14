#ALPHABETS


#SAHANA
#Letter A
n=7
for row in range(n):
    for column in range(n):
        if row==0 or column==0 or row==n//2 or column==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * * 
*           * 
*           * 
* * * * * * * 
*           * 
*           * 
*           * 
'''

#SAHANA
#Letter B
n=7
for row in range(n):
    for column in range(n):
        if ( column==0 or row==0 or row==n-1 or row==n//2 or column==n-1) :
            print('*', end='')
        else:
            print(' ', end='')
    print() 

#OUTPUT
'''
* * * * * * *
*           *
*           *
* * * * * * *
*           *
*           *
* * * * * * *
'''

#SAHANA
#Letter C
n=7
for row in range(n):
    for column in range(n):
        if row==0 or column==0 or row==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * * 
*
*
*
*
*
* * * * * * * 
'''

#SAHANA
#Letter D
n=7
for row in range(n):
    for column in range(n):
        if row==0 or column==0 or row==n-1 or column==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * *
'''

#SAHANA
#Letter E
n=7
for row in range(n):
    for column in range(n):
        if row==0 or column==0 or row==n-1 or row==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * *
*
*
* * * * * * *
*
*
* * * * * * *
'''

#SAHANA
#Letter F
n=7
for row in range(n):
    for column in range(n):
        if row==0 or column==0 or row==n//2 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * *
*
*
* * * * * * *
*
*
*
'''

#SAHANA
#Letter G
n=7
for row in range(n):
    for column in range(n):
        if (row==0 or column==0 or row==n-1 ) or (column>=n//2 and row==n//2   ) or (column==n-1 and row>=n//2 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() 

#OUTPUT
'''
* * * * * * *
*
*
*     * * * *
*           *
*           *
* * * * * * *
'''

#SAHANA
#Letter H
n=7
for row in range(n):
    for column in range(n):
        if  column==0  or column==n-1 or row==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
*           *
*           *
*           *
* * * * * * *
*           *
*           *
*           *
'''

#SAHANA
#Letter I
n=7
for row in range(n):
    for column in range(n):
        if row==0 or row==n-1 or column==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * *
      *
      *
      *
      *
      *
* * * * * * *
'''



#DIYA 
#Letter J
n=7
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or (row==n-1 and col<=n//2) or (col==0 and row>=n//2):
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * *
      *
      *
*     *
*     *
*     *
* * * *
'''


#DIYA 
#Letter K
n=7
for row in range(n):
    for col in range(n):
        if col==0 or row+col==n//2 or row-col==n//2:
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
*     *
*   *
* *
*
* *
*   *
*     *
'''


#DIYA 
#Letter L
n=7
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1:
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
*
*
*
*
*
*
* * * * * * *
'''

#DIYA
#Letter M
n=7
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and row<=n//2) or (row+col==n-1 and row<=n//2):
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
*           *
* *       * *
*   *   *   *
*     *     *
*           *
*           *
*           *
'''


#DIYA
#Letter N
n=7
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
*           *
* *         *
*   *       *
*     *     *
*       *   *
*         * *
*           *
'''


#DIYA 
#Letter O
n=7
for row in range(n):
    for col in range(n):
        if (row==0 or row==n-1) and (col>0 and col<n-1) or (col==0 or col==n-1) and (row>0 and row<n-1):
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
  * * * * *
*           *
*           *
*           *
*           *
*           *
  * * * * *
'''


#DIYA
#Letter P
n=7
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2 and col<n-1 or col==n-1 and row<=n//2:
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * *
*           *
*           *
* * * * * * *
*
*
*
'''


#DIYA
#Letter Q
n=7
for row in range(n):
    for col in range(n):
        if (row==0 or row==n-2) and (col>0 and col<n-1) or (col==0 or col==n-1) and (row>0 and row<n-2):
            print('*',end=' ') 
        elif row==col and row>=n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
  * * * * *
*           *
*           *
*     *     *
*       *   *
  * * * * *
            *
'''


#DIYA 
#Letter R
n=7
for row in range(n):
    for col in range(n):
        if col==0 or (row==0 or row==n//2) and col<n-1 or col==n-1 and row<n//2 or (row==col and row>n//2):
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

#OUTPUT
'''
* * * * * * *
*           *
*           *
* * * * * *
*       *
*         *
*           *
'''
