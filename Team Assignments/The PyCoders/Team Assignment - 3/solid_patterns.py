
'''
Left Aligned Right Angle Triangle
or
Increasing Triangle Pattern

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
    
    
    
    
    




'''
Left Aligned Inverted Right Angle Triangle
or
Decreasing Triangle Pattern

* * * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


'''

n = int(input())
for row in range(n):
    for col in range(row,n):
        print("*",end=" ")
    print()
        