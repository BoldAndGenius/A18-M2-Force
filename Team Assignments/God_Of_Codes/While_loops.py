"""
61.Write a program to extract all the string values present in the list collection only if the last character is upper case. Concatenate the extracted output using ‘*’.

"""
user_input = input("Enter elements separated by commas: ")
elements = [item.strip() for item in user_input.split(',')]
result = ''
index = 0
# print('debug')
while index < len(elements):
    if type(elements[index]) is str:
        last_char = elements[index][len(elements[index]) - 1]
        if 65 <= ord(last_char) <= 90:
            if result:
                result += '*'
            result += elements[index]
    index += 1
print(result)

"""

62.write a program to extract all the list data items present in list collection only if it is having middle value , that value is integer and having even number at start

"""

# list_collection = [[1, 2, 3, 4, 5],[10, 12, 14],[6, 7, 8, 9, 10],[1, 2, 'a', 5, 6],[2, 4, 6],[8, 10, 12, 14, 16]]
# result = []
# index = 0

# while index < len(list_collection):
#     current_list = list_collection[index]

#     if len(current_list) % 2 == 1:
#         middle_value = current_list[len(current_list) // 2]

#         if type(middle_value) == int:
#             first_digit = abs(middle_value)

#             while first_digit >= 10:
#                 first_digit //= 10
#             if first_digit % 2 == 0:
#                 result.append(current_list)

#     index += 1
# print(result)

"""

63.Write a program to get the following output
input= ‘just looking like wow’
output= ‘jusT LOOKING Like a wow’

"""

# input_str = 'just looking like wow'
# words = input_str.split()

# i = 0
# while i < len(words):
#     if i == 0:
#         words[i] = words[i][:3] + words[i][3].upper() if len(words[i]) > 3 else words[i].capitalize()
#     elif i == 1:
#         words[i] = words[i].upper()
#     elif i == 2:
#         words[i] = words[i].capitalize()
#     elif i == 3:
#         words[i] = 'a ' + words[i]
#     i += 1

# output_str = ' '.join(words)
# print(output_str)


"""

64.Program to find the common elements in two sets using a while loop

"""

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# common_elements = set()
# list1 = list(set1)
# list2 = list(set2)
# i = 0
# j = 0

# while i < len(list1) and j < len(list2):
#     if list1[i] == list2[j]:
#         common_elements.add(list1[i])
#         i += 1
#         j += 1
#     elif list1[i] < list2[j]:
#         i += 1
#     else:
#         j += 1
# print("Common elements:", common_elements)


"""

76.Write a program to get the following output
input1=’11001010’
input2=’01110010’
output=4(to count how many positions are having same value)
from itertools import count, product

"""

# input1="11001010"
# input2="01110010"
# count = 0
# output = 0
# while count < len(input1):
#     if input1[count] == input2[count]:
#         output += 1
#     count += 1
# print(output)

"""

77..Write a program to get the following output
input=[1,2,3,4,5,6]
value=3
output=[1,2,3][4,5,6]
If value=2
output=[1,2][3,4][5,6]

"""
# ip=[1,2,3,4,5,6]
# value = int(input("Enter a value:"))
# count = 0
# index = 0
# output = []
# while count < len(ip) // value:
#     list1=[]
#     in_index = 0
#     while in_index < value:
#         list1.append(ip[index])
#         in_index += 1
#         index += 1
#     output.append(list1)
#     count += 1
# print(output)

"""

78.Write a program to check weather the given number is spy number or not i.e, 1*2*3=1+2+3

"""
# ip = int(input("Enter a number:"))
# num = ip
# sum = 0
# prodt = 1
# while num > 0:
#     digit = num % 10
#     sum += digit
#     prodt *= digit
#     num //= 10
# if sum == prodt:
#     print(f"{ip} is a spy number")
# else:
#     print(f"{ip} is not a spy number")

"""

79..Write a program to check weather the given number is Xylem number or not i.e, 1234 →
1+4=2+3

"""
# ip = input("Enter a number:")
# dig = [int(ip[i]) for i in range(len(ip))]
# Extreme_dig = []
# Mid_dig = []
# Sum_of_Extreme_dig = 0
# Sum_of_Mid_dig = 0
# index = 0
# while index < len(dig):
#     if index == 0 or index == len(dig) - 1:
#         Extreme_dig.append(dig[index])
#     else:
#         Mid_dig.append(dig[index])
#     index += 1
# index = 0
# while index < len(Extreme_dig):
#     Sum_of_Extreme_dig += Extreme_dig[index]
#     index += 1
# index = 0
# while index < len(Mid_dig):
#     Sum_of_Mid_dig += Mid_dig[index]
#     index += 1
# if Sum_of_Extreme_dig == Sum_of_Mid_dig:
#     print(f"{ip} is a Xylem number.")
# else:
#     print(f"{ip} is not a Xylem number.")

"""

80.Write a program to check weather the given number is phloem number or not
I.e, 12345 → 1+5 != 2+3+4

"""
# ip = input("Enter a number:")
# dig = [int(ip[i]) for i in range(len(ip))]
# Extreme_dig = []
# Mid_dig = []
# Sum_of_Extreme_dig = 0
# Sum_of_Mid_dig = 0
# index = 0
# while index < len(dig):
#     if index == 0 or index == len(dig) - 1:
#         Extreme_dig.append(dig[index])
#     else:
#         Mid_dig.append(dig[index])
#     index += 1
# index = 0
# while index < len(Extreme_dig):
#     Sum_of_Extreme_dig += Extreme_dig[index]
#     index += 1
# index = 0
# while index < len(Mid_dig):
#     Sum_of_Mid_dig += Mid_dig[index]
#     index += 1
# if Sum_of_Extreme_dig != Sum_of_Mid_dig:
#     print(f"{ip} is a Phloem number.")
# else:
#     print(f"{ip} is not a Phloem number.")