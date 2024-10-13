
'''
Left Aligned Right Angle Triangle

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 

'''

n = int(input())  # 11
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()