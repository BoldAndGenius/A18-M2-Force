
# Pattern Programming - 1 
# Given an integer n, Draw a square. 

n = int(input("Enter a Number : "))

for row in range(n):
  for col in range(n):
    if row ==0 or row == n-1 or col==0 or col==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()