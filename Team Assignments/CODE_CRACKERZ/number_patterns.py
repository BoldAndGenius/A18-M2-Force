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
Pattern-4
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
Pattern-5
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
Pattern-6
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
Pattern-7
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
Pattern-8
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
    print(" " * (num-row),end=" ")
    for col in range(row):
        if count > 9:
            count =1
        print(count,end=" ")
        count+=1
    print()


'''
Pattern-10
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







