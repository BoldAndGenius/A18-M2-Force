n= int(input('enter'))
num=1
for row in range(1,n):
    for col in range(1,row+1):
        print(num,end=' ')
        num+=1
    print()
'''
 1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36   
'''



 # for row in range(1,n):
print()

num=1
for row in range(1,n):
    print(" "*(n-row),end="")
    for col in range(1,row+1):
        print(col,end=' ')
        num+=1
    print()


''''
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
   1 2 3 4 5 6
  1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8
 '''

# print() 

num=1
for row in range(1,n):
    for col in range(1,row+1):
        print(col,end=' ')
    print()
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
'''
A