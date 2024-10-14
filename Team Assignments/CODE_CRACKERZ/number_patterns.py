'''
Pattern-1
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
num = int(input("Enter a number: "))
for row in range(num+1):
    for col in range(row):
        print(row,end=" ")
    print()


'''
Pattern-2
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
num = int(input("Enter a number:"))
count = 0
for row in range(num,0,-1):
    count+=1
    for col in range(1,row+1):
        print(count,end=" ")
    print()


'''
Pattern-3
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
num = int(input("Enter a number :"))
for row in range(num,0,-1):
    count = row
    for col in range(row):
        print(count,end=" ")
    print()


'''
Pattern-4
1 
2 3 
4 5 6 
7 8 9 10
11 12 13 14 15
'''
num = int(input("Enter a number:"))
count = 1
for row in range(1,num+1):
    for col in range(row):
        print(count,end=" ")
        count+=1
    print()

    
'''
Pattern-5
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
'''
num =int(input("Enter a number:"))
count=1
for row in range(1,num+1):
    for col in range(row):
        print(count,end=" ")
        count+=2
    print()


'''
Pattern-6
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
num =int(input("Enter a number:"))
for row in range(1,num+1):
    for col in range(row):
        print(col+1,end=" ")
    print()


'''
Pattern-7
1
2 3
4 5 6
7 8 9 1
2 3 4 5 6
'''
num =int(input("Enter a number:"))
count=1
for row in range(1,num+1):
    for col in range(row):
        if count > 9:
            count =1
        print(count,end=" ")
        count+=1
    print()


'''
Pattern-8
9
8 7
6 5 4
3 2 1 9
8 7 6 5 4
'''
num =int(input("Enter a number:"))
count=9
for row in range(1,num+1):
    for col in range(row):
        if count < 1:
            count =9
        print(count,end=" ")
        count-=1
    print()


'''
Pattern-9
         1
       2 3
     4 5 6
   7 8 9 1
 2 3 4 5 6
'''
num =int(input("Enter a number:"))
count=1
for row in range(1,num+1):
    print("  " * (num-row),end=" ")
    for col in range(row):
        if count > 9:
            count =1
        print(count,end=" ")
        count+=1
    print()


'''
Pattern-10
     1
    2 3
   4 5 6
  7 8 9 1
 2 3 4 5 6
'''
num =int(input("Enter a number:"))
count=1
for row in range(1,num+1):
    print(" " * (num-row),end=" ")
    for col in range(row):
        if count > 9:
            count =1
        print(count,end=" ")
        count+=1
    print()


'''
Pattern-11
1 2 3 4 5
  6 7 8 9
    1 2 3
      4 5
        6
'''
num =int(input("Enter a number:"))
count=1
for row in range(num,0,-1):
    print("  " * (num-row),end=" ")
    for col in range(row):
        if count > 9:
            count =1
        print(count,end=" ")
        count+=1
    print()
    

'''
12)
    1 
    3 3 
    5 5 5 
    7 7 7 7 
    9 9 9 9 9
'''
n = int(input("Enter num:"))
num = 1
for row in range(n):
    for col in range(row+1):
        print(num,end=" ")
    num += 2
    print()
    
    
    
'''
13)
    1 
    2 1 
    3 2 1 
    4 3 2 1 
    5 4 3 2 1
'''
n = int(input('Enter num:'))
num = 1
for row in range(n):
    row_num = num
    for col in range(row+1):
        print(row_num,end=" ")
        row_num -= 1
    num += 1
    print()
    
    
    
'''
14) 
    5 4 3 2 1 
    4 3 2 1 
    3 2 1 
    2 1 
    1
'''
n = int(input("Enter num:"))
num = n
for row in range(n,0,-1):
    row_num = num
    for col in range(row):
        print(row_num,end=' ')
        row_num -= 1
    num -= 1
    print()
 
 
    
'''
15)
    1  
    2  4  
    3  6  9  
    4  8  12  16  
    5  10  15  20  25  
    6  12  18  24  30  36  
    7  14  21  28  35  42  49  
    8  16  24  32  40  48  56  64
'''
n = int(input("Enter num:"))
num = 1
for row in range(n):
    row_num = 1
    for col in range(row+1):
        print(num * row_num,end=" ")
        row_num += 1
    num += 1
    print()
   
    
    
'''
16)
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
'''

n = int(input("Enter num:"))
for row in range(1,n+1):
    num = 1
    print(" " * (n - row),end=" ")
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()
   
    
    
'''
17)
            1
          1 2 3
        1 2 3 4 5
      1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8 9
'''
n = int(input("Enter num:"))
for row in range(1,2*n,2):
    print(" " * ((2*n - 1) - row),end=" ")
    num = 1
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()
   
    
    
'''
18)
    1 2 3 4 5 6 7 8 9
      1 2 3 4 5 6 7
        1 2 3 4 5
          1 2 3
            1
'''
n = int(input("Enter num:"))
for row in range(2*n,1,-2):
    print(" " * ((2*n - 1) - row),end=" ")
    num = 1
    for col in range(row-1):
        print(num,end=" ")
        num += 1
    print()
    
    
    
'''
19)
            1
          1 2 3
        1 2 3 4 5
      1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8 9
      1 2 3 4 5 6 7
        1 2 3 4 5
          1 2 3
            1
'''
n = int(input("Enter num:"))
for row in range(1,2*n,2):
    print(" " * ((2*n - 1) - row),end=" ")
    num = 1
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()
for row in range((2*n-2),1,-2):
    print(" " * (2*n - row),end=" ")
    num = 1
    for col in range(row-1):
        print(num,end=" ")
        num += 1
    print()
    

'''
20)
    1 2 3 4 5 6 7 8 9
      1 2 3 4 5 6 7
        1 2 3 4 5
          1 2 3
            1
          1 2 3
        1 2 3 4 5 
      1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8 9
'''
n = int(input("Enter num:"))
for row in range(2*n-1,1,-2):
    print(" " * ((2*n ) - row),end=" ")
    num = 1
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()
for row in range(1,2*n,2):
    print(" " * ((2*n)- row),end=" ")
    num = 1
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()
    
    
'''
21)
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
     1 2 3 4
      1 2 3
       1 2
        1
'''
n = int(input("Enter num:"))
for row in range(1,n+1):
    print(" " * (n - row),end=" ")
    num = 1
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()
for row in range(n-1,0,-1):
    print(" " * (n - row),end=" ")
    num = 1
    for col in range(row):
        print(num,end=" ")
        num += 1
    print()

'''
22)  1 
    2 1 
   3 2 1 
  4 3 2 1 
 5 4 3 2 1 
 '''
num= int(input( "enter the number :"))
for row in range(1,num+1):
    print(' '*(num-row),end=" ")
    for col in range(row ,0,-1):
        print(col,end=' ')  
    print()

'''
23)
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5 
'''
num= int(input( "enter the number :"))
for row in range(1,num+1):
    for col in range(1,num+1):
        if col<=row:
            print(row,end=' ')
        else:
            print(col,end=' ')
    print()    
    
    '''
    24)

  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1 
      3 2 1 
    5 4 3 2 1 
  7 6 5 4 3 2 1 
  
'''
num = int(input("Enter Number:"))
for row in range(2*num-1,1,-2):
    print(" " * ((2*num ) - row),end=" ")
    for col in range(1,row+1):
        print(col,end=" ")
    print()
for row in range(1,2*num,2):
    print(" " * ((2*num)- row),end=" ")
    for col in range(row,0,-1):
        print(col,end=" ")      
    print()
    






