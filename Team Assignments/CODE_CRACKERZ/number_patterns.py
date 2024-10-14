
'''
Pattern-1
1 
2 3 
4 5 6 
7 8 9 10
11 12 13 14 15
'''
num =int(input("Enter a number:"))
count=1
for row in range(1,num+1):
    for col in range(row):
        print(count,end=" ")
        count+=1
    print()

    
'''
Pattern-2
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
Pattern-3
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
Pattern-4
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

