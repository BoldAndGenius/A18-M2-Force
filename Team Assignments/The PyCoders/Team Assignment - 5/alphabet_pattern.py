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
    
    
    
    
    
    
    
    
    
    
    
    
'''
Alphabet Pattern - 3

A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 

'''

char = 'A'
n = int(input())
for row in range(n):
    for col in range(n):
        print(char,end=" ")
        char = chr(ord(char)+1)
    print()
    
    
    




'''
Alphabet Pattern - 4

A B C D E 
B C D E F 
C D E F G 
D E F G H 
E F G H I 

 
'''

n = int(input())
char = 'A'
for row in range(n):
    new = char
    for col in range(n):
        print(new,end=" ")
        new = chr(ord(new)+1)
    char = chr(ord(char)+1)
    print()
    
    
    



'''
Alphabet Pattern - 5

A B C B A 
B C D C B 
C D E D C 
D E F E D 
E F G F E 


'''

n = int(input())
char = 'A'
for row in range(n):
    new = char  
    for col in range(n):
        if col<n//2:
            print(new,end=" ")
            new = chr(ord(new)+1)
        else:
            print(new,end=" ")
            new = chr(ord(new)-1)
    print()
    char = chr(ord(char)+1)