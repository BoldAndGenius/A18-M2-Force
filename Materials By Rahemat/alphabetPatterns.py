'''Patterns By Rahemat J'''

'''A pattern'''
# n = 11
# for row in range(n):
#     for col in range(n):
#         if (col == 0 and row >= n // 2) or (col == n - 1 and row >= n // 2) or ((row+col) == n // 2) or((col-row) == n // 2) or row == n // 2:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''B pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or col in (0, n - 1) or row == n // 2:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''C pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or col == 0:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''D pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or col in (0, n - 1) or (row == 0 and col != n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''E pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or col == 0  or (row == n // 2 and col <= n - 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''F pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == 0  or (row == n // 2 and col <= n - 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''G pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or col == 0 or (col == n - 1 and row >= n // 2) or (col >= n // 2 and row == n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''H pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row == n // 2 or col in (0, n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''I pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if col == n // 2 or (row == 0 and 1 <= col < n - 1) or (row == n - 1 and 1 <= col < n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''J pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if col == n // 2 or (row == 0 and 1 <= col < n - 1) or (row == n - 1 and col < n // 2) or (col == 0 and row > n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''K pattern'''
# n = 5
# for row in range(n):
#     for col in range(n):
#         if col == 0 or ((row-col) == 1 and row >= n // 2) or ((row+col) == (n // 2) + 1 and row < n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''L pattern'''
# n = 5
# for row in range(n):
#     for col in range(n):
#         if col == 0 or (row == n - 1 and col < n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''M pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or (row == col and col <= n // 2) or ((row+col) == n - 1 and row <= n // 2):
#             print(("*"), end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''N pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or row == col:
#             print(("*"), end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''O pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or col in (0, n - 1) or (row == 0 and col != n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''P pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == 0 or (col == n - 1 and row <= n // 2) or row == n // 2:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''Q pattern'''
# n = 9
# for row in range(n):
#     for col in range(n):
#         if (row in (0, n - 3) and col <= n - 3) or (col == 0 and row <= n - 3) or (col == n - 3 and row <= n - 3) or (row > n // 2 and row == col) :
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''R pattern'''
# n = 5
# for row in range(n):
#     for col in range(n):
#         if col == 0 or (col == n-1 and row <= n // 2) or row == 0 or row == n // 2 or (row == col and row >= n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''S pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or (col == 0 and row < n // 2) or (col == n - 1 and row > n // 2) or row == n // 2:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''T pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if col == n // 2 or (row == 0):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''U pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if (col == 0 and row <= n // 2) or (col == n - 1 and row <= n // 2) or ((row-col) == n // 2) or ((row+col) == n + 2 and col >= n // 2 and row >= n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''V pattern'''
n = 5
for row in range(n):
    for col in range(n):
        # if :
            print((row,col), end = "")
        # else:
            # print(" ", end = " ")
    print()

'''W pattern'''
# n = 5
# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or ( (row+col) == n - 1 and row >= n // 2) or (row == col and row >= n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''X pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row == col or (row+col) == n - 1:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''Y pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if (row == col and row <= n // 2) or ((row+col) == n - 1 and row <= n // 2) or (col == n // 2 and row > n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

'''Z pattern'''
# n = 7
# for row in range(n):
#     for col in range(n):
#         if row in (0, n - 1) or row+col == n - 1:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
