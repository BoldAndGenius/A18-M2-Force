# # Hallow square pattern

# n = int(input("Enter Number: "))
# for row in range(n):
#     for col in range(n):
#         if row in (0,n-1) or col in (0,n-1):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
# '''     * * * * * 
#         *       *
#         *       *
#         *       *
#         * * * * *        '''

n = int(input("Enter Number: "))
for row in range(n):
    for col in range(n//2):
        print('*',end=' ')
    else:
        print(' ',end=' ')
    print()
        

        
