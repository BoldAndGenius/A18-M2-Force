# Alphabet Pattern 


'''
Alphabet Pattern - 1: 

A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 



'''

n = int(input())
char = 'A'
for row in range(n):
    for col in range(n):
        print(char,end=" ")
    char = chr(ord(char)+1)
    print()
    
    
    








'''
Alphabet Pattern - 2

A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 

'''


n = int(input())
for row in range(n):
    char = 'A'
    for col in range(n):
        print(char,end=" ")
        char = chr(ord(char)+1)
    print()