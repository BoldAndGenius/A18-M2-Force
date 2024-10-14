# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n=5
for row in range(1,n+1):
    for col in range(row):
        print(row,end=' ')
    print()
print()



# 1
# 2 3
# 4 5 6
# 7 8 9 10

n=4
res=1
for row in range(1,n+1):
    for col in range(row):
        print(res,end=' ')
        res+=1
    print()
print()



# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
for row in range(1,n+1):
    res=1
    for col in range(row):
        print(res,end=' ')
        res+=1
    print()
print()



# 1
# 3   5
# 7   9   11
# 13   15   17   19
# 21   23   25   27   29

n=5
res=1
for row in range(1,n+1):
    for col in range(row):
        print(res,end='   ')
        res+=2
    print()
print()



# 1 to 9 integers in 7 x7 matrix

# 1
# 2 3
# 4 5 6
# 7 8 9 1
# 2 3 4 5 6
# 7 8 9 1 2 3
# 4 5 6 7 8 9 1

n=7
res=1
for row in range(1,n+1):
    for col in range(row):
        print(res,end=' ')
        res+=1
        if res>9:
            res=1
    print()
print()



#       1
#      2 3
#     4 5 6
#    7 8 9 1
#   2 3 4 5 6
#  7 8 9 1 2 3
# 4 5 6 7 8 9 1

n=7
res=1
for row in range(n):
    for col in range(n-row-1):
        print(' ',end='')
    for col in range(row+1):
        print(res,end=' ')
        res+=1
        if res>9:
            res=1
    print()
print()




#             1
#           2 3
#         4 5 6
#       7 8 9 1
#     2 3 4 5 6
#   7 8 9 1 2 3
# 4 5 6 7 8 9 1

n=7
res=1
for row in range(n):
    for col in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print(res,end=' ')
        res+=1
        if res>9:
            res=1
    print()
print()


# 1 2 3 4 5 6 7
#  8 9 1 2 3 4
#   5 6 7 8 9
#    1 2 3 4
#     5 6 7
#      8 9
#       1

n=7
res=1
for row in range(n,0,-1):
    for col in range(n-row):
        print(' ',end='')
    for col in range(row):
        print(res,end=' ')
        res+=1
        if res>9:
            res=1
    print()
print()


# 1 2 3 4 5 6 7
#   8 9 1 2 3 4
#     5 6 7 8 9
#       1 2 3 4
#         5 6 7
#           8 9
#             1

n=7
res=1
for row in range(n,0,-1):
    for col in range(n-row):
        print(' ',end=' ')
    for col in range(row):
        print(res,end=' ')
        res+=1
        if res>9:
            res=1
    print()
print()


# 1 2 3 4 5 6 7
# 8 9 1 2 3 4
# 5 6 7 8 9
# 1 2 3 4
# 5 6 7
# 8 9
# 1

n=7
res=1
for row in range(n,0,-1):
    for col in range(row):
        print(res,end=' ')
        res+=1
        if res>9:
            res=1
    print()
print()