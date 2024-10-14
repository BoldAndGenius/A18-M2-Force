'''
1 
2 3 
4 5 6 
7 8 9 10
11 12 13 14 15

'''
num =int(input("Enter a number:"))
n=1
for row in range(1,num+1):
    for col in range(row):
        print(n,end=" ")
        n+=1
    print()